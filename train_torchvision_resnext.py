from ikomia import dataprocess


# --------------------
# - Interface class to integrate the process with Ikomia application
# - Inherits dataprocess.CPluginProcessInterface from Ikomia API
# --------------------
class IkomiaPlugin(dataprocess.CPluginProcessInterface):

    def __init__(self):
        dataprocess.CPluginProcessInterface.__init__(self)

    def getProcessFactory(self):
        from train_torchvision_resnext.train_torchvision_resnext_process import TrainResnextFactory
        # Instantiate process object
        return TrainResnextFactory()

    def getWidgetFactory(self):
        from train_torchvision_resnext.train_torchvision_resnext_widget import TrainResnextWidgetFactory
        # Instantiate associated widget object
        return TrainResnextWidgetFactory()
