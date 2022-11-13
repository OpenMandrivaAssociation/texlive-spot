Name:		texlive-spot
Version:	22408
Release:	1
Summary:	Spotlight highlighting for Beamer
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/beamer-contrib/spot
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/spot.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/spot.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/spot.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package allows dramatic highlighting of words and phrases
by painting shapes around them. It is chiefly intended for use
in Beamer presentations, but it can be used in other document
classes as well.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/spot/spot.sty
%doc %{_texmfdistdir}/doc/latex/spot/README
%doc %{_texmfdistdir}/doc/latex/spot/spot.pdf
#- source
%doc %{_texmfdistdir}/source/latex/spot/spot.dtx
%doc %{_texmfdistdir}/source/latex/spot/spot.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
