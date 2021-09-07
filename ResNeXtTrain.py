from ikomia import dataprocess


# --------------------
# - Interface class to integrate the process with Ikomia application
# - Inherits dataprocess.CPluginProcessInterface from Ikomia API
# --------------------
class ResNeXtTrain(dataprocess.CPluginProcessInterface):

    def __init__(self):
        dataprocess.CPluginProcessInterface.__init__(self)

    def getProcessFactory(self):
        from ResNeXtTrain.ResNeXtTrain_process import ResNeXtTrainProcessFactory
        # Instantiate process object
        return ResNeXtTrainProcessFactory()

    def getWidgetFactory(self):
        from ResNeXtTrain.ResNeXtTrain_widget import ResNeXtTrainWidgetFactory
        # Instantiate associated widget object
        return ResNeXtTrainWidgetFactory()
