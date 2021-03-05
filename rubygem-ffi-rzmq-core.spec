# Generated from ffi-rzmq-core-1.0.7.gem by gem2rpm -*- rpm-spec -*-
%global gem_name ffi-rzmq-core

Name: rubygem-%{gem_name}
Version: 1.0.7
Release: 1%{?dist}
Summary: This gem provides only the FFI wrapper for the ZeroMQ (0mq) networking library
License: MIT
URL: http://github.com/chuckremes/ffi-rzmq-core
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# The zeromq provides unversioned soname only in its devel subpackage,
# which pulls in too many unnecessary dependencies
Patch0: %{name}-%{version}-specify_libzmq_soname_version.patch
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(rspec)
BuildRequires: rubygem(ffi)
BuildRequires: zeromq
# RPM does not generate zeromq require automatically.
Requires: zeromq

BuildArch: noarch

%description
This gem provides only the FFI wrapper for the ZeroMQ (0mq) networking
library.
Project can be used by any other zeromq gems that want to provide their own
high-level Ruby API.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version}

%patch0 -p1

%build
# Create the gem as gem install only works on a gem file
gem build ../%{gem_name}-%{version}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}
rspec -Ilib:$(dirs +1)/%{gem_extdir_mri} spec
popd

%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE
%{gem_libdir}
%{gem_spec}
%exclude %{gem_instdir}/.*
%exclude %{gem_cache}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/History.txt
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/ffi-rzmq-core.gemspec
%{gem_instdir}/spec

%changelog
* Fri Mar 5 2021 Jarek Prokop <jprokop@redhat.com> - 1.0.7-1
- Initial package
