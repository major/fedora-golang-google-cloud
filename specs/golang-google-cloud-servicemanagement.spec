# Generated by go2rpm 1.9.0
%bcond_without check
%global debug_package %{nil}

%global submodule       servicemanagement

# https://github.com/googleapis/google-cloud-go
%global goipath         cloud.google.com/go/%{submodule}
%global forgeurl        https://github.com/googleapis/google-cloud-go
Version:                1.9.0
%global tag             %{submodule}/v%{version}

%gometa

# Remove in F40.
%global godevelheader %{expand:
Obsoletes:      golang-cloud-google-devel <= 0.103.0
}

%global common_description %{expand:
Google Cloud Client Libraries for the %{submodule} API.}

%global golicenses      LICENSE
%global godocs          CHANGES.md CODE_OF_CONDUCT.md CONTRIBUTING.md\\\
                        README.md RELEASING.md SECURITY.md debug.md\\\
                        migration.md testing.md

Name:           %{goname}
Release:        %autorelease
Summary:        Google Cloud Client Libraries for %{submodule} API

License:        Apache-2.0 AND BSD-3-Clause
URL:            %{gourl}
Source:         %{gosource}

%description %{common_description}

%gopkg

%prep
%goprep -s %{_builddir}/%{extractdir}/%{submodule}
%autopatch -p1

%generate_buildrequires
%go_generate_buildrequires

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
%autochangelog

