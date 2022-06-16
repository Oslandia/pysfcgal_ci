echo "deb http://deb.debian.org/debian stretch-backports main" > /etc/apt/sources.list.d/backports.list
apt-get update -qq
apt-get install -y wget cmake libboost1.67-all-dev libgmp-dev libmpfr-dev make xz-utils

cmake --version

wget https://github.com/CGAL/cgal/releases/download/v5.4/CGAL-5.4.tar.xz
tar xJf CGAL-5.4.tar.xz
cd CGAL-5.4 && mkdir build && cd build && cmake .. && make && make install

cd /opt
git clone https://gitlab.com/Oslandia/SFCGAL.git
mkdir -p /opt/SFCGAL/build_release
cd /opt/SFCGAL/build_release
cmake \
    -DCMAKE_BUILD_TYPE=Release \
    /opt/SFCGAL
make
make install
