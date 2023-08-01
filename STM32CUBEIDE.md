# Using the pqm4 Library in STM32CubeIDE

# Contents
- [Using the pqm4 Library in STM32CubeIDE](#using-the-pqm4-library-in-stm32cubeide)
- [Contents](#contents)
  - [Introduction](#introduction)
  - [Prerequisites](#prerequisites)
  - [Install Git](#install-git)
  - [Enable Developer Mode](#enable-developer-mode)
  - [Clone the pqm4 Library](#clone-the-pqm4-library)
  - [STM32CubeIDE Project](#stm32cubeide-project)

## Introduction

This guide demonstrates how to quickly and easily use the pqm4 implementations in the STM32CubeIDE. This library includes a number of highly optimized implementations of post-quantum cryptographic algorithms to run on an ARM Cortex-M4 microcontroller.

## Prerequisites

To follow this guide, you will need a to have the STM32CubeIDE installed and have a basic knowledge of how to use it. If you do not have this installed please refer to this [guide](https://github.com/QUB-ARM-STM32/User-Guide/blob/master/STM32CubeIDE/README.md). It is also recommended that you have a basic knowledge of [git](https://git-scm.com/).

I have produced this guide for Windows, however it should be similar for Linux and MacOS.

## Install Git

To clone the repository correctly we will need to download and install [git for windows](https://gitforwindows.org/).

When installing you must ensure to enable symbolic links on windows. This is required as the pqm4 library uses symbolic links within its codebase.

## Enable Developer Mode

To ensure the symbolic links are correctly converted to windows shortcuts you must enable developer mode on your machine. To do this follow the steps below:

- Windows 10
    - `Settings` -> `Update & Security` -> `For developers` -> `Developer Mode`

- Windows 11
    - `Settings` -> `Privacy & Security` -> `For developers` -> `Developer Mode`

## Clone the pqm4 Library

To clone the pqm4 library correctly run the following command from `Git Bash`:

```bash
git clone --recursive -c core.symlinks=true https://github.com/mupq/pqm4.git
```

This will clone the pqm4 library and ensure that the symbolic links are converted to windows shortcuts.

## STM32CubeIDE Project

We can now create a new project within the STM32CubeIDE. Ensure to set up the project with default values for the peripherals.

As the pqm4 splits up the different systems into different folders for each systems, but the file names are the same within we will use a one project for one crypto system to keep things simple. In this example I will be using `kyber768`.

- drag common into core
- drag kyber768_speed into core
- 