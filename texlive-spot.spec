%global tl_name spot
%global tl_revision 22408

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1
Release:	%{tl_revision}.1
Summary:	Spotlight highlighting for Beamer
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/beamer-contrib/spot
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/spot.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/spot.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/spot.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package allows dramatic highlighting of words and phrases by
painting shapes around them. It is chiefly intended for use in Beamer
presentations, but it can be used in other document classes as well.

