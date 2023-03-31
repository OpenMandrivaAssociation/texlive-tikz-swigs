Name:		texlive-tikz-swigs
Version:	59889
Release:	2
Summary:	Horizontally and vertically split elliptical nodes
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/tikz-swigs
License:	lppl1.3c gpl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tikz-swigs.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tikz-swigs.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides horizontally and vertically split
elliptical (pairs of) nodes in TikZ. The package name derives
from the fact that split ellipses of this type are used to
represent Single-World Intervention Graph (SWIG) models which
are used in counterfactual causal inference.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/tikz-swigs
%doc %{_texmfdistdir}/doc/latex/tikz-swigs

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
