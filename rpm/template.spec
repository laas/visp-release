Name:           ros-lunar-visp
Version:        3.0.1
Release:        4%{?dist}
Summary:        ROS visp package

Group:          Development/Libraries
License:        GPLv2
URL:            http://www.ros.org/wiki/visp
Source0:        %{name}-%{version}.tar.gz

Requires:       Coin2-devel
Requires:       bzip2-devel
Requires:       lapack-devel
Requires:       libX11-devel
Requires:       libdc1394-devel
Requires:       libdmtx-devel
Requires:       libfreenect-devel
Requires:       libjpeg-turbo-devel
Requires:       libpng-devel
Requires:       libusb-devel
Requires:       libv4l-devel
Requires:       libxml2-devel
Requires:       ogre-devel
Requires:       ois-devel
Requires:       ros-lunar-opencv3
Requires:       zbar-devel
BuildRequires:  Coin2-devel
BuildRequires:  bzip2-devel
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  lapack-devel
BuildRequires:  libX11-devel
BuildRequires:  libdc1394-devel
BuildRequires:  libdmtx-devel
BuildRequires:  libfreenect-devel
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  libpng-devel
BuildRequires:  libusb-devel
BuildRequires:  libv4l-devel
BuildRequires:  libxml2-devel
BuildRequires:  ogre-devel
BuildRequires:  ois-devel
BuildRequires:  ros-lunar-opencv3
BuildRequires:  zbar-devel

%description
ViSP standing for Visual Servoing Platform is a modular cross platform library
that allows prototyping and developing applications using visual tracking and
visual servoing technics at the heart of the researches done by Inria Lagadic
team. ViSP is able to compute control laws that can be applied to robotic
systems. It provides a set of visual features that can be tracked using real
time image processing or computer vision algorithms. ViSP provides also
simulation capabilities. ViSP can be useful in robotics, computer vision,
augmented reality and computer animation.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/lunar" \
        -DCMAKE_PREFIX_PATH="/opt/ros/lunar" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/lunar

%changelog
* Tue Nov 14 2017 Fabien Spindler <Fabien.Spindler@inria.fr> - 3.0.1-4
- Autogenerated by Bloom

* Tue Nov 14 2017 Fabien Spindler <Fabien.Spindler@inria.fr> - 3.0.1-3
- Autogenerated by Bloom

* Fri Jun 23 2017 Fabien Spindler <Fabien.Spindler@inria.fr> - 3.0.1-2
- Autogenerated by Bloom

* Fri Jun 23 2017 Fabien Spindler <Fabien.Spindler@inria.fr> - 3.0.1-1
- Autogenerated by Bloom

* Fri Jun 23 2017 Fabien Spindler <Fabien.Spindler@inria.fr> - 3.0.1-0
- Autogenerated by Bloom

