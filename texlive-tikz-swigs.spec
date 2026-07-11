%global tl_name tikz-swigs
%global tl_revision 59889

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Horizontally and vertically split elliptical nodes
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pgf/contrib/tikz-swigs
License:	lppl1.3c gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tikz-swigs.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tikz-swigs.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides horizontally and vertically split elliptical
(pairs of) nodes in TikZ. The package name derives from the fact that
split ellipses of this type are used to represent Single-World
Intervention Graph (SWIG) models which are used in counterfactual causal
inference.

