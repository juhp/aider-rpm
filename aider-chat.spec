%global pypi_name aider-chat

#%%define _python_dist_allow_version_zero 1

# Empty %files file aider-chat-0.82.3-build/aider_chat-0.82.3/debugsourcefiles.list
%define debug_package %{nil}

Name: %{pypi_name}
Version: 0.83.1
License: Apache-2.0
Release: 1%{?dist}
Summary: Aider is AI pair programming in your terminal
URL:     https://github.com/Aider-AI/aider
#Source0: %%{pypi_source %%{pypi_name} %%{version}}
# https://pypi.org/project/aider-chat/#files
Source0: https://files.pythonhosted.org/packages/fe/4b/20088dcb8b03598654ce473e5444771049e159874a8838cbc74bc34bc193/aider_chat-0.83.1.tar.gz
BuildRequires: chrpath
#BuildRequires: cmake
#BuildRequires: gcc
#BuildRequires: gcc-c++
#BuildRequires: gcc-fortran
#BuildRequires: git-core
BuildRequires: libtree-sitter-devel
BuildRequires: openblas-devel
BuildRequires: pyjson5
BuildRequires: pyproject-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-distro
BuildRequires: python3-dotenv
BuildRequires: python3-flake8
BuildRequires: python3-httpx
BuildRequires: python3-huggingface-hub
BuildRequires: python3-jsonschema
BuildRequires: python3-markdown-it-py
BuildRequires: python3-networkx
BuildRequires: python3-numpy
BuildRequires: python3-pip
BuildRequires: python3-pycodestyle
BuildRequires: python3-pyflakes
BuildRequires: python3-pygments
BuildRequires: python3-rsa
BuildRequires: python3-scipy
BuildRequires: python3-setuptools
BuildRequires: python3-tqdm
BuildRequires: python3-watchfiles
BuildRequires: python3-wheel
# cd /var/lib/mock/fedora-rawhide-x86_64/root/builddir/build/BUILD/aider-chat-0.82.3-build/BUILDROOT
# echo ./usr/lib/python3.13/site-packages/* | sed -e 's/^.//' -e 's/ \./ /g' | xargs frpq rawhide
BuildRequires: NFStest
BuildRequires: b43-tools
BuildRequires: dxf2gcode
BuildRequires: netstat-monitor
BuildRequires: python3-GitPython
BuildRequires: python3-aiohappyeyeballs
BuildRequires: python3-aiosignal
BuildRequires: python3-annotated-types
BuildRequires: python3-anyio
BuildRequires: python3-backoff
BuildRequires: python3-beautifulsoup4
BuildRequires: python3-cachetools
BuildRequires: python3-certifi
BuildRequires: python3-click
BuildRequires: python3-configargparse
BuildRequires: python3-dateutil
BuildRequires: python3-demjson
BuildRequires: python3-dialog
BuildRequires: python3-diff-match-patch
BuildRequires: python3-diskcache
BuildRequires: python3-filelock
BuildRequires: python3-flake8
BuildRequires: python3-fusepy
BuildRequires: python3-gitdb
BuildRequires: python3-google-api-client
BuildRequires: python3-google-api-core
BuildRequires: python3-google-auth
BuildRequires: python3-google-auth-httplib2
BuildRequires: python3-google-cloud-core
BuildRequires: python3-google-cloud-dns
BuildRequires: python3-google-cloud-storage
BuildRequires: python3-google-resumable-media
BuildRequires: python3-googleapis-common-protos
BuildRequires: python3-grpc-google-iam-v1
BuildRequires: python3-grpcio-status
BuildRequires: python3-httplib2
BuildRequires: python3-hwdata
BuildRequires: python3-importlib-metadata
BuildRequires: python3-importlib-resources
BuildRequires: python3-jinja2
BuildRequires: python3-jinja2+i18n
BuildRequires: python3-jsonschema-specifications
BuildRequires: python3-lc3
BuildRequires: python3-libconcord
BuildRequires: python3-libftdi
BuildRequires: python3-libs
BuildRequires: python3-matrix-synapse-ldap3
BuildRequires: python3-novaclient-os-networks
BuildRequires: python3-packaging
BuildRequires: python3-pathspec
BuildRequires: python3-pefile
BuildRequires: python3-pexpect
BuildRequires: python3-polib
BuildRequires: python3-policycoreutils
BuildRequires: python3-prompt-toolkit
BuildRequires: python3-proto-plus
BuildRequires: python3-ptyprocess
BuildRequires: python3-pyasn1-modules
BuildRequires: python3-pycodestyle
BuildRequires: python3-pycparser
BuildRequires: python3-pydantic
BuildRequires: python3-pydantic+email
BuildRequires: python3-pydantic+timezone
BuildRequires: python3-pyflakes
BuildRequires: python3-pygments-style-solarized
BuildRequires: python3-pypandoc
BuildRequires: python3-pyparsing
BuildRequires: python3-pyperclip
BuildRequires: python3-pyspf
BuildRequires: python3-rich
BuildRequires: python3-rsa
BuildRequires: python3-six
BuildRequires: python3-smmap
BuildRequires: python3-socksio
BuildRequires: python3-soupsieve
BuildRequires: python3-typing-inspection
BuildRequires: python3-uritemplate
BuildRequires: python3-vtk
BuildRequires: python3-wcwidth
BuildRequires: python3-xmltramp
BuildRequires: python3-zipp
BuildRequires: shyaml
BuildRequires: winpdb

%description
Aider code assistant


#%%dynamic_buildrequires
#%%pyproject_buildrequires -N requirements.txt


%prep
%setup -q -n aider_chat-%{version}
sed -i -e 's/<3.13/<3.14/' pyproject.toml
sed -i -e 's/\(.*\)==.*/\1/g' requirements.txt

# voice.py backtracing via pydub with "No module named 'audioop'"
sed -i -e 's/import models, prompts, voice/import models, prompts #, voice/' aider/commands.py

%build


%install
pip install --root %{buildroot} .

for i in %{buildroot}%{python3_sitearch}/tree_sitter_language_pack/bindings/*.so; do
    chrpath -d $i
done

sed -i -e 's!/usr/bin/env python!/usr/bin/env python3!' %{buildroot}%{python3_sitelib}/aider/coders/{base_coder.py,search_replace.py}

for i in $(ls %{buildroot}%{_bindir}/* | grep -v aider$); do
    rm $i
done


%files
%license LICENSE.txt
%doc README.md
%{_bindir}/aider
%{python3_sitelib}/*
%{python3_sitearch}/*


%changelog
* Tue May 13 2025 Jens Petersen <petersen@redhat.com> - 0.83.1-1
- initial pip install package
