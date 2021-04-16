# Parser Creation

Files associated with the creation of your own custom parsers using an example of "show service-routing database" on IOS-XE. This command is sufficiently obscure that a community based parser does not already exist.

# Getting Started

The repo does not have a mandatory requirement for access to a Lab Cisco IOS-XE device. A sample script is provided if you have access to a Lab device but otherwise the main learning aspects are covered from using static data obtained from a lab Cisco router.

# 1. make sure pyATS (including the libraries) is installed if using the scratch_test.py file to run this against a CSR1000v/IOS-XE router
bash$ pip install pyats[full]

# 2. clone this repository into your environment
bash$ git clone https://github.com/gwoodwa1/ParserCreation

Tested Against Python 3.8.6 using CSR1000v on IOS-XE 16.6.4

Contribution

Please feel free to open PR against this repository for changes or bug fixes you may wish to add.
