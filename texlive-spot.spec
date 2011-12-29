# revision 22408
# category Package
# catalog-ctan /macros/latex/contrib/beamer-contrib/spot
# catalog-date 2011-05-10 01:20:26 +0200
# catalog-license lppl1.3
# catalog-version 1.1
Name:		texlive-spot
Version:	1.1
Release:	1
Summary:	Spotlight highlighting for Beamer
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/beamer-contrib/spot
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/spot.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/spot.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/spot.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
