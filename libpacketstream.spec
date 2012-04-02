#
%define name    libpacketstream 

Name:			%{name}
Version:		0.1.4
%define rel		1
Release:		%mkrel %rel
Summary:		interface of the packetstream thread-safe ring buffer
License:		MIT-Style
Group:			System/Libraries
URL:			https://github.com/ienorand/packetstream
BuildRoot:      	%_tmppath/%{name}-%{version}-%{release}-buildroot
Source0:		libpacketstream-0.1.4.tar.bz2
ExclusiveArch:		i586 x86_64
BuildRequires:		cmake
BuildRequires:		gcc gcc-c++ make


%description	
Interface of the 'packetstream' thread-safe ring buffer.

%prep  
%setup -q -n %{name}-%{version}

%build 
cmake -D CMAKE_INSTALL_PREFIX=$RPM_BUILD_ROOT .
%make

%install 
rm -rf $RPM_BUILD_ROOT
%makeinstall
mkdir $RPM_BUILD_ROOT/usr
mv $RPM_BUILD_ROOT/include $RPM_BUILD_ROOT/usr/include
%ifarch i586
mv $RPM_BUILD_ROOT/lib $RPM_BUILD_ROOT/usr/lib
%endif
%ifarch x86_64
mv $RPM_BUILD_ROOT/lib $RPM_BUILD_ROOT/usr/lib64
%endif 

%clean
rm -rf $RPM_BUILD_ROOT

%files -n %{name}
%defattr(0755,root,root)
%{_libdir}/libpacketstream*
%{_includedir}/*

