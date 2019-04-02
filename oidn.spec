Name:		oidn
Version:	0.8.2
Release:	4%{?dist}
Summary:	Library of denoising filters for images rendered with ray tracing

License:	ASL 2.0
URL:		https://openimagedenoise.github.io/
Source0:	https://github.com/OpenImageDenoise/%{name}/releases/download/v%{version}/%{name}-%{version}.src.tar.gz

# Library only available of x86_64 arch
ExclusiveArch:	x86_64

BuildRequires:	cmake >= 3.13.0
BuildRequires:	gcc-c++
BuildRequires:	python3-devel
BuildRequires:	tbb-devel

%description
An open source library of high-performance, high-quality denoising
filters for images rendered with ray tracing.

%package	libs
Summary:	Libraries for %{name}

%description	libs
The %{name}-libs package contains shared library for %{name}.

%package        devel
Summary:	Development files for %{name}
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}

%description	devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package	docs
Summary:	Documentation for %{name}
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}
BuildArch:	noarch

%description	docs
The %{name}-docs package contains documentation for %{name}.

%prep
%autosetup


%build
%cmake -DCMAKE_VERBOSE_MAKEFILE:BOOL=TRUE \
	.
%make_build


%install
%make_install

# Remove duplicated documentation
rm -rf %{buildroot}%{_docdir}/OpenImageDenoise


%files
%license LICENSE.txt
%doc CHANGELOG.md 
%{_bindir}/denoise

%files libs
%{_libdir}/cmake/OpenImageDenoise
%{_libdir}/libOpenImageDenoise.so.*

%files docs
%doc README.md readme.pdf 

%files devel
%{_includedir}/OpenImageDenoise
%{_libdir}/libOpenImageDenoise.so

%changelog
* Tue Apr 02 2019 Luya Tshimbalanga <luya@fedoraproject.org> - 0.8.2-4
- Use spaces on line 47
- Make -doc subpackage noarch
- Make -doc subpackage requiring main package

* Mon Apr 01 2019 Luya Tshimbalanga <luya@fedoraproject.org> - 0.8.2-3
- Move versioned so-files to libs subpackage
- Move unversioned so-files to devel subpackage

* Mon Apr 01 2019 Luya Tshimbalanga <luya@fedoraproject.org> - 0.8.2-2
- Add subpackage for large doc files
- Move .so files to devel subpackage
- Fix library path
- Remove unneeded clearance

* Sun Mar 31 2019 Luya Tshimbalanga <luya@fedoraproject.org> - 0.8.2-1
- Initial packaging
