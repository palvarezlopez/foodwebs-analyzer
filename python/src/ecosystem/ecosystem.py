# import libraries
from common.inputParameters import InputParameters
from common.printer import Printer
from ecosystem.ode.odeSolver import ODESolver
from ecosystem.proportions import Proportions
from ecosystem.analysis.donorControlModel import DonorControlModel
from ecosystem.analysis.generalModel import GeneralModel
from ecosystem.data.foodWebData import FoodWebData
from ecosystem.data.symbolicData import SymbolicData


# class food web data (used for read input files)
class Ecosystem:

    # Initializing, receive filename and fill all food web data
    def __init__(self, inputParameters: InputParameters, printer: Printer, fileName: str, customInitialBiomass: bool):
        # init folder and latex document
        printer.initFolderAndLatexDocument(fileName)
        # declare food web data
        self.foodWebData = FoodWebData(inputParameters, printer, fileName, customInitialBiomass)
        # declare symbolic data
        self.symbolicData = SymbolicData(inputParameters, self.foodWebData)
        # declare proportions associated with this food web data
        self.proportions = Proportions()
        # calculate donor control model
        if (inputParameters.calculateDonorControlModel):
            self.donorControlModel = DonorControlModel(inputParameters, printer, self.symbolicData, self.foodWebData)
        # calculate general model
        if (inputParameters.calculateGeneralModel):
            self.generalModel = GeneralModel(inputParameters, printer, self.symbolicData, self.foodWebData, self.proportions, self.donorControlModel)
        # check if calculate biomass dynamic
        if (inputParameters.calculateBiomassDynamic):
            self.odeSolver = ODESolver(inputParameters, printer, self.generalModel, self.symbolicData, self.foodWebData, self.proportions)
        # write output files
        printer.writeOutputFiles(self.foodWebData.food_web_filename)

    # foodWeb data
    foodWebData: FoodWebData

    # symbolic data
    symbolicData: SymbolicData

    # donor control model (either analytic or graphic)
    donorControlModel: DonorControlModel

    # general model (either analytic or graphic)
    generalModel: GeneralModel

    # ODE Solver
    odeSolver: ODESolver

    # proportions
    proportions: Proportions