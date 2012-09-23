#define debug_package	%{nil}
%define name    libpacketstream 
%define release		1.1
%define develname %mklibname -d packetstream

Name:			%{name}
Version:		0.1.4
Release:		%{release}
Summary:		interface of the packetstream thread-safe ring buffer
License:		MIT
Group:			System/Libraries
URL:			https://github.com/ienorand/packetstream
Source0:		https://nodeload.github.com/ienorand/packetstream/tarball/libpacketstream-0.1.4.tar.bz2
ExclusiveArch:		i586 x86_64
BuildRequires:		cmake
BuildRequires:		gcc gcc-c++ make


%description	
Interface of the 'packetstream' thread-safe ring buffer.

%prep  
%setup -q -n %{name}-%{version}
rm -fr debian

%build 
cmake -D CMAKE_INSTALL_PREFIX=$RPM_BUILD_ROOT .
%make

%install 
%makeinstall
install -d  $RPM_BUILD_ROOT%{_libdir}
install -d  $RPM_BUILD_ROOT%{_includedir}
mv $RPM_BUILD_ROOT/include/*.h $RPM_BUILD_ROOT%{_includedir}
mv $RPM_BUILD_ROOT/lib/* $RPM_BUILD_ROOT%{_libdir}
rm -fr $RPM_BUILD_ROOT/include
rm -fr $RPM_BUILD_ROOT/lib

%files -n %{name}
%defattr(0755,root,root)
%{_libdir}/libpacketstream.so*

#----------
%package -n %{develname}
Summary: Development files for %{name}
Provides: %{name}-devel = %{version}-%{release}
Requires: %{name} = %{version}-%{release}

%description -n %{develname}
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}

%files -n %{develname}
%{_includedir}/*




