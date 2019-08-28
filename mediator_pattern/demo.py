from abc import ABC, abstractmethod
from enum import Enum
from typing import List


class DeviceType(Enum):
    """设备类型"""
    speaker_type = 1
    microphone_type = 2
    camera = 3


class DevicItem:
    """设备项"""

    def __init__(self, id, name, type: DeviceType):
        self.__id = None
        self.__name = None
        self.__type = None

        self.id = id
        self.name = name
        self.type = type

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: DeviceType):
        assert isinstance(type, DeviceType), TypeError("type must is DevicType")
        self.__type = type

    def __str__(self):
        return f"id: {self.id}, type:{self.type}, name: {self.name}"


class DeviceMgr(ABC):

    @abstractmethod
    def enumerate(self) -> List[DevicItem]:
        """枚举类列表"""
        pass

    @abstractmethod
    def active(self, device_id):
        """选择要使用的设备"""
        pass

    @abstractmethod
    def get_cur_device_id(self):
        pass


class SpeakerMgr(DeviceMgr):

    def __init__(self):
        self.__cur_device_id = None

    def enumerate(self) -> List[DevicItem]:
        devices = [
            DevicItem("1234", "Realtek High Definition Audio", DeviceType.speaker_type),
            DevicItem("2342", "NVIDIA High Definition Audio", DeviceType.speaker_type),
        ]
        return devices

    def active(self, device_id):
        self.__cur_device_id = device_id

    def get_cur_device_id(self):
        return self.__cur_device_id


class DeviceUtil:
    """设备工具类"""

    def __init__(self):
        self.__device_type2mer = {}

    def set_mgr(self, type: DeviceType, mgr: DeviceMgr):
        self.__device_type2mer[type] = mgr

    def get_device_mgr(self, type: DeviceType) -> DeviceMgr:
        return self.__device_type2mer[type]

    def get_devices(self, type: DeviceType):
        return self.get_device_mgr(type).enumerate()

    def get_cur_device_id(self, type: DeviceType):
        return self.get_device_mgr(type).get_cur_device_id()

    def active(self, type: DeviceType, id):
        self.get_device_mgr(type).active(id)


if __name__ == "__main__":
    device_util = DeviceUtil()
    device_util.set_mgr(DeviceType.speaker_type, SpeakerMgr())
    speaker_devices = device_util.get_devices(DeviceType.speaker_type)
    if speaker_devices:
        device_util.active(DeviceType.speaker_type, speaker_devices[0].id)
        for device in speaker_devices:
            print(device)

        print(f"当前设备为:{device_util.get_cur_device_id(DeviceType.speaker_type)}")
