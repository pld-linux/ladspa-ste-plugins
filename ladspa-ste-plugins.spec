Summary:	STE (stereo effects) LADSPA plugins
Summary(pl.UTF-8):	Wtyczki LADSPA STE (efektów stereofonicznych)
Name:		ladspa-ste-plugins
Version:	0.0.2
Release:	1
License:	GPL v2+
Group:		Applications/Sound
Source0:	http://kokkinizita.linuxaudio.org/linuxaudio/downloads/STE-plugins-%{version}.tar.bz2
# Source0-md5:	9a6b41cb8594221f7a87cb8662e8699d
Patch0:		%{name}-make.patch
URL:		http://kokkinizita.linuxaudio.org/linuxaudio/ladspa/index.html
BuildRequires:	ladspa-devel
BuildRequires:	libstdc++-devel
Requires:	ladspa-common
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoprovfiles	%{_libdir}/ladspa

%description
STE (stereo offects) LADSPA plugins.

%description -l pl.UTF-8
Wtyczki LADSPA STE (efektów stereofonicznych).

%prep
%setup -q -n STE-plugins-%{version}
%patch -P0 -p1

%build
CPPFLAGS="%{rpmcppflags}" \
CXXFLAGS="%{rpmcxxflags}" \
LDFLAGS="%{rpmldflags}" \
%{__make} \
	CXX="%{__cxx}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/ladspa

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	LADSPA_LIB_DIR=%{_libdir}/ladspa

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS
%attr(755,root,root) %{_libdir}/ladspa/stereo-plugins.so
