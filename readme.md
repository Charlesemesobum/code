# Installation

Installation steps are mentioned in [INSTALL.md](https://github.com/CuautliG/Group_F_Simulation_of_a_manufacturing_facility/tree/master/INSTALL.md)

# Usage

To run, you must first install it. Then you can follow instructions mentioned in
[User_Manual.md](https://github.com/CuautliG/Group_F_Simulation_of_a_manufacturing_facility/tree/master/doc/User_Manual.md).

# File Structure

The correct file structure (after installing GSL library should be follow and run the binary)

├── INSTALL.md 	-> Installation Guide
├── LICENSE 	-> License file
├── Makefile 	-> Makefile
├── README.md 	-> Readme file
├── bin 	-> Binary directory
├── doc
│
│
├── data 	
│   ├── input
│   │   ├── servinsp1.dat
│   │   ├── servinsp22.dat
│   │   ├── servinsp23.dat
│   │   ├── ws1.dat
│   │   ├── ws2.dat
│   │   └── ws3.dat
│   │
│   │
│   └── output
│       └── results.csv
│
├── include 	-> Header files
│   ├── data_types.h
│   ├── export.h
│   ├── main.h
│   ├── read_config.h
│   ├── read_data.h 
│   └── work_flow.h
│
└── src 	
   ├── export.c
   ├── main.c 	
   ├── read_config.c
   ├── read_data.c
   ├── work_flow.c
   └── sensor.c



# Documentation

The User manual is available [here](https://github.com/CuautliG/Group_F_Simulation_of_a_manufacturing_facility/wiki).
The developer manual is available [here](https://github.com/CuautliG/Group_F_Simulation_of_a_manufacturing_facility/wiki).

# License

This project is licensed under the GPL 2.0 License - see the LICENSE.md file for details

# Acknowledgements

Thank to Dr. Cristina Ruiz Martin for providing guidance on how to develop the software.
