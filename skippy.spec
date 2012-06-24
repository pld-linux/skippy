Summary:	Full-screen task-switcher for X11
Summary(pl):	Pe�noekranowy prze��cznik zada� dla X11
Name:		skippy
Version:	0.4.1
Release:	1
License:	GPL
Group:		X11/Window Managers
Source0:	http://thegraveyard.org/files/%{name}-%{version}.tar.bz2
# Source0-md5:	4d0d2b05f8f1357ceb80754f52a90991
Patch0:		%{name}-home_etc.patch
URL:		http://thegraveyard.org/skippy.php
BuildRequires:	home-etc-devel
BuildRequires:	imlib2-devel
BuildRequires:	pkgconfig
BuildRequires:	xft-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Skippy is what (I think) is best described as a full-screen
task-switcher for X11. It tries to provide an alternative when
taskbars or regular task-switchers aren't the most efficient way of
switching tasks (like when you have a lot of applications open). When
activated (currently only through a hotkey), it will arrange and scale
snapshots of all windows on the current desktop and it'll let you pick
a window using a mouse or a keyboard. Yes, this is also what expocity
and Apple's Expose do (yeah, I know, Expose does more than just this),
but I don't like metacity (expocity is a 'hacked up' version of that)
and I don't have a Mac.

%description -l pl
Skippy mo�e by� najlepiej okre�lony jako pe�noekranowy prze��cznik
zada� dla X11. Stanowi alternatyw� dla pask�w zada� i tradycyjnych
prze��cznik�w zada�, kt�re nie s� najefektywniejsz� metod�
prze��czania mi�dzy zadaniami (zw�aszcza, je�li ma si� du�o
uruchomionych aplikacji. Kiedy zostanie aktywowany (obecnie tylko przy
pomocy klawisza), u�o�y i przeskaluje miniaturki wszystkich okien na
bie��cym pulpicie i pozwoli na wyb�r okna przy pomocy klawiatury lub
myszy. Tak samo robi to expocity i Expose Apple'a, ale expocity to
osobny zarz�dca okien a Expose jest tylko dla Mac�w.

%prep
%setup -q
%patch0 -p1

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	PREFIX=%{_prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG skippyrc-default
%attr(755,root,root) %{_bindir}/*
