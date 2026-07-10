%global tl_name continue
%global tl_revision 79461

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.2
Release:	%{tl_revision}.1
Summary:	Prints continuation marks on pages of multipage documents
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/continue
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/continue.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/continue.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/continue.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides for a variety of continuation indicators on pages
when the text continues on the following page. The default is to only
mark odd pages, but all pages can be marked and the marking can be
stopped or started at any point.

