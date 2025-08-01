cmake_minimum_required(VERSION 3.10)
project(HELLOWORLD)

# Set C++ standard
set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Include header files
include_directories(include)

# Collect all source files
file(GLOB SOURCES src/*.cpp src/*.cxx)

# Define the executable
add_executable(HelloWorld ${SOURCES})

# Install the executable to bin directory
install(TARGETS HelloWorld DESTINATION bin)

# Install the headers to include directory
install(DIRECTORY include/ DESTINATION include)

# Optional: allow user to control the installation prefix
# Example: cmake -DCMAKE_INSTALL_PREFIX=/my/custom/path ..
