%define snapshot 20240111
%undefine _debugsource_packages

Name: slibtool
Version: 0.5.35
Release: %{?snapshot:0.%{snapshot}.}1
Source0: https://github.com/midipix-project/slibtool/archive/refs/heads/main.tar.gz
Summary: Drop-in replacement for libtool
URL: https://github.com/midipix-project/slibtool
License: Custom BSD-like
Group: Development/Tools

%description
`slibtool` is an independent reimplementation of the widely used libtool,
written in C. `slibtool` is designed to be a clean, fast, easy-to-use
libtool drop-in replacement, and is accordingly aimed at package authors,
distro developers, and system integrators. `slibtool` maintains compatibility
with libtool in nearly every aspect of the tool's functionality as well as
semantics, leaving out (or turning into a no-op) only a small number of
features that are no longer needed on modern systems.

Being a compiled binary, and although not primarily written for the sake of
performance, building a package with `slibtool` is often faster than with its
script-based counterpart. The resulting performance gain would normally vary
between packages, and is most noticeable in builds that invoke libtool a large
number of times, and which are characterized by the short compilation duration
of individual translation units.

%prep
%autosetup -p1 -n %{name}-main
# Looks like autoconf, but isn't
./configure \
%if %{cross_compiling}
	--target=%{_target_platform} \
%endif
	--prefix=%{_prefix} \
	--libdir=%{_libdir}

%build
%make_build

%install
%make_install

%files
%{_bindir}/clibtool
%{_bindir}/clibtool-shared
%{_bindir}/clibtool-static
%{_bindir}/dlibtool
%{_bindir}/dlibtool-shared
%{_bindir}/dlibtool-static
%{_bindir}/rclibtool
%{_bindir}/rdclibtool
%{_bindir}/rdlibtool
%{_bindir}/rlibtool
%{_bindir}/slibtool
%{_bindir}/slibtool-shared
%{_bindir}/slibtool-static