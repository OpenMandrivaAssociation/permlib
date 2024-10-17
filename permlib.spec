Name:           permlib
Version:        0.2.8
Release:        6%{?dist}
Summary:        Library for permutation computations

License:        BSD
URL:            https://www.math.uni-rostock.de/~rehn/software/%{name}.html
Source0:        http://www.math.uni-rostock.de/~rehn/software/%{name}-%{version}.tar.gz
# Doxygen config file written by Jerry James <loganjerry@gmail.com>
Source1:        %{name}-Doxyfile
Patch0:		%{name}-0.2.8-boost_mt.patch
BuildArch:      noarch

BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  ghostscript
BuildRequires:  gmp-devel
BuildRequires:  texlive

%description
PermLib is a callable C++ library for permutation computations.
Currently it supports set stabilizer and in-orbit computations, based on
bases and strong generating sets (BSGS).  Additionally, it computes
automorphisms of symmetric matrices and finds the lexicographically
smallest set in an orbit of sets.

%package devel
Summary:        Header files for developing programs that use PermLib
Requires:       boost-devel

%description devel
PermLib is a callable C++ library for permutation computations.
Currently it supports set stabilizer and in-orbit computations, based on
bases and strong generating sets (BSGS).  Additionally, it computes
automorphisms of symmetric matrices and finds the lexicographically
smallest set in an orbit of sets.

This package contains header files for developing programs that use
PermLib.

%prep
%setup -q
%patch0 -p1
sed "s/@VERSION@/%{version}/" %{SOURCE1} > Doxyfile

%build
%if 0%{?fedora}
%cmake .
%else
%cmake
%endif
make %{?_smp_mflags}

# Build the documentation
%if 0%{?fedora}
%else
cd ..
%endif
mkdir doc
doxygen
rm -f doc/html/installdox

%install
# No install target is generated in the makefile, and
# DESTDIR=$RPM_BUILD_ROOT cmake -P cmake_install.cmake
# does nothing, so we do it by hand.

# Install the header files
mkdir -p $RPM_BUILD_ROOT%{_includedir}
cp -a include/%{name} $RPM_BUILD_ROOT%{_includedir}

%check
ctest

%files devel
%doc AUTHORS CHANGELOG LICENSE doc/html
%{_includedir}/permlib

%changelog
* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 30 2013 Petr Machata <pmachata@redhat.com> - 0.2.8-5
- Rebuild for boost 1.54.0
- Remove -mt suffix from boost_unit_testing_framework DSO
  (permlib-0.2.8-boost_mt.patch)

* Sun Feb 10 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 0.2.8-4
- Rebuild for Boost-1.53.0

* Sat Feb 09 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 0.2.8-3
- Rebuild for Boost-1.53.0

* Fri Feb  8 2013 Jerry James <loganjerry@gmail.com> - 0.2.8-2
- Adjust BRs for TeXLive 2012

* Thu Sep 27 2012 Jerry James <loganjerry@gmail.com> - 0.2.8-1
- New upstream release
- Drop upstreamed patch

* Wed Sep 26 2012 Jerry James <loganjerry@gmail.com> - 0.2.7-1
- New upstream release
- Update Doxyfile
- Add -test patch to fix two test failures

* Mon Aug  6 2012 Jerry James <loganjerry@gmail.com> - 0.2.6-4
- Rebuild for boost 1.50
- Update Doxyfile

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri May  4 2012 Jerry James <loganjerry@gmail.com> - 0.2.6-2
- BR gmp-devel
- Add comment on origin of Doxyfile

* Fri Mar 16 2012 Jerry James <loganjerry@gmail.com> - 0.2.6-1
- Initial RPM
