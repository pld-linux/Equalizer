#
# Conditional build:
%bcond_without	apidocs		# do not build and package API docs
#
Summary:	Equalizer - parallel rendering framework
Summary(pl.UTF-8):	Equalizer - szkielet do równoległego renderowania
Name:		Equalizer
Version:	2.1.0
Release:	1
License:	LGPL v2.1
Group:		Libraries
#Source0Download: https://github.com/Eyescale/Equalizer/releases
Source0:	https://github.com/Eyescale/Equalizer/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	fc882b9ae31ee49b83f32c15094e656a
URL:		http://www.equalizergraphics.com/
BuildRequires:	Collage-devel >= 1.7.0
BuildRequires:	Eyescale-CMake >= 2017.05
BuildRequires:	Lunchbox-devel >= 1.16.0
BuildRequires:	OpenGL-devel
BuildRequires:	Pression-devel >= 2.0.0
BuildRequires:	Qt5Core-devel >= 5
BuildRequires:	Qt5Gui-devel >= 5
BuildRequires:	Qt5Widgets-devel >= 5
#BuildRequires:	Qt5OpenGL-devel >= 4.6 #?
BuildRequires:	Servus-devel >= 1.5.1
BuildRequires:	bison
BuildRequires:	boost-devel >= 1.41.0
BuildRequires:	cmake >= 3.1
%{?with_apidocs:BuildRequires:	doxygen}
BuildRequires:	flex
# glew-mx?
BuildRequires:	glew-devel >= 1.6
BuildRequires:	hwloc-devel >= 1.3
BuildRequires:	hwsd-devel >= 2.0.1
BuildRequires:	libgomp-devel
BuildRequires:	libstdc++-devel
BuildRequires:	opencv-devel >= 2.0
BuildRequires:	pkgconfig
BuildRequires:	python-devel >= 2
BuildRequires:	vmmlib >= 1.13.0
BuildRequires:	xorg-lib-libX11-devel
# GLStats>=0.3.2 0.3.3-snap? Deflect>=0.14.0
# OpenSceneGraph>=3.0 VRPN>=07.30 DisplayCluster>=0.4 magellan spnav? opencv?
Requires:	Collage >= 1.7.0
Requires:	Lunchbox >= 1.16.0
Requires:	Pression >= 2.0.0
Requires:	Servus >= 1.5.1
Requires:	hwsd >= 2.0.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Equalizer is the standard middleware to create and deploy parallel
OpenGL-based applications. It enables applications to benefit from
multiple graphics cards, processors and computers to scale the
rendering performance, visual quality and display size. An Equalizer
application runs unmodified on any visualization system, from a simple
workstation to large scale graphics clusters, multi-GPU workstations
and Virtual Reality installations.

%description -l pl.UTF-8
Equalizer to standardowa warstwa pośrednia do tworzenia i wdrażania
zrównoleglonych aplikacji opartych na OpenGL-u. Pozwala aplikacjom
wykorzystywać wiele kart graficznych, procesorów i komputerów w celu
skalowania wydajności renderingu oraz jakości i rozmiaru obrazu.
Aplikacje Equalizera działają bez modyfikacji na każdym systemie
wizualizacji, od prostych stacji roboczych do wielkich klastrów
graficznych, na stacjach roboczych z wieloma GPU oraz instalacjach
wirtualnej rzeczywistości.

%package devel
Summary:	Header files for Equalizer libraries
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotek Equalizer
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	Collage-devel >= 1.7.0
Requires:	Lunchbox-devel >= 1.16.0
Requires:	glew-devel >= 1.6

%description devel
Header files for Equalizer libraries.

%description devel -l pl.UTF-8
Pliki nagłówkowe bibliotek Equalizer.

%package apidocs
Summary:	Equalizer API documentation
Summary(pl.UTF-8):	Dokumentacja API bibliotek Equalizer 
Group:		Documentation

%description apidocs
API documentation for Equalizer libraries.

%description apidocs -l pl.UTF-8
Dokumentacja API bibliotek Equalizer.

%package examples
Summary:	Examples for Equalizer package
Summary(pl.UTF-8):	Przykłady do pakietu Equalizer
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description examples
Examples for Equalizer package.

%description examples -l pl.UTF-8
Przykłady do pakietu Equalizer.

%prep
%setup -q

rmdir CMake/common
ln -sf /usr/share/Eyescale-CMake CMake/common

%build
install -d build
cd build
%cmake .. \
	-DBUILDYARD_DISABLED=ON
%{__make}

%if %{with apidocs}
doxygen doc/Doxyfile
%endif

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}
%{__mv} $RPM_BUILD_ROOT%{_datadir}/Equalizer/examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/Equalizer/doc

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ACKNOWLEDGEMENTS AUTHORS CHANGES.md LICENSE.txt README.md doc/{FAQ,PLATFORMS,README.{IB,Linux,OpenMP,VirtualGL,paracomp,udt},RelNotes.md}
%attr(755,root,root) %{_bindir}/eVolve
%attr(755,root,root) %{_bindir}/eVolveConverter
%attr(755,root,root) %{_bindir}/eqAsync
%attr(755,root,root) %{_bindir}/eqHello
%attr(755,root,root) %{_bindir}/eqPixelBench
%attr(755,root,root) %{_bindir}/eqPly
%attr(755,root,root) %{_bindir}/eqPlyConverter
%attr(755,root,root) %{_bindir}/eqServer
%attr(755,root,root) %{_bindir}/eqThreadAffinity
%attr(755,root,root) %{_bindir}/eqWindowAdmin
%attr(755,root,root) %{_bindir}/seqPly
%attr(755,root,root) %{_libdir}/libEqualizer.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libEqualizer.so.180
%attr(755,root,root) %{_libdir}/libEqualizerAdmin.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libEqualizerAdmin.so.180
%attr(755,root,root) %{_libdir}/libEqualizerFabric.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libEqualizerFabric.so.180
%attr(755,root,root) %{_libdir}/libEqualizerServer.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libEqualizerServer.so.180
%attr(755,root,root) %{_libdir}/libSequel.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libSequel.so.180
%attr(755,root,root) %{_libdir}/libtriply.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtriply.so.180
%dir %{_datadir}/Equalizer
%{_datadir}/Equalizer/configs
%{_datadir}/Equalizer/data

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libEqualizer.so
%attr(755,root,root) %{_libdir}/libEqualizerAdmin.so
%attr(755,root,root) %{_libdir}/libEqualizerFabric.so
%attr(755,root,root) %{_libdir}/libEqualizerServer.so
%attr(755,root,root) %{_libdir}/libSequel.so
%attr(755,root,root) %{_libdir}/libtriply.so
%{_includedir}/eq
%{_includedir}/seq
%{_includedir}/triply
%{_pkgconfigdir}/Equalizer.pc
%{_datadir}/Equalizer/CMake

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%doc build/doc/html/*
%endif

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
