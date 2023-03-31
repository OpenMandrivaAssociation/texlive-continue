Name:		texlive-continue
Version:	49449
Release:	2
Summary:	Prints 'continuation' marks on pages of multipage documents
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/continue
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/continue.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/continue.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/continue.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides for a variety of continuation indicators
on pages when the text continues on the following page. The
default is to only mark odd pages, but all pages can be marked
and the marking can be stopped or started at any point.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/continue
%{_texmfdistdir}/tex/latex/continue
%doc %{_texmfdistdir}/doc/latex/continue

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
