%define major 0
%define libname %mklibname packetstream %{major}
%define devname %mklibname packetstream -d

Summary:	Interface of the packetstream thread-safe ring buffer
Name:		libpacketstream
Version:	0.1.4
Release:	3
License:	MIT
Group:		System/Libraries
Url:		https://github.com/ienorand/packetstream
Source0:	https://nodeload.github.com/ienorand/packetstream/tarball/%{name}-%{version}.tar.bz2
BuildRequires:	cmake

%description
Interface of the 'packetstream' thread-safe ring buffer.

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	Shared library for %{name}
Conflicts:	%{name} < 0.1.4-2
Obsoletes:	%{name} < 0.1.4-2

%description -n %{libname}
Shared library for %{name}.

%files -n %{libname}
%{_libdir}/libpacketstream.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Development files for %{name}
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}
Conflicts:	%{name} < 0.1.4-2

%description -n %{devname}
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}

%files -n %{devname}
%{_libdir}/libpacketstream.so
%{_includedir}/*

#----------------------------------------------------------------------------

%prep
%setup -q
rm -fr debian

%build
%cmake -DMLIBDIR=%{_lib}
%make

%install
%makeinstall_std -C build
