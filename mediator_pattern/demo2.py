class HouseInfo:
    """房屋信息"""

    def __init__(self, area, price, has_window, has_bathroom, has_kitchen, address, owner):
        self.__area = area
        self.__price = price
        self.__has_window = has_window
        self.__has_bathroom = has_bathroom
        self.__has_kitchen = has_kitchen
        self.__address = None
        self.__owner = owner

        self.address = address

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, address):
        assert isinstance(address, str), TypeError(f"address is str, not {type(address)}")
        self.__address = address

    def get_owner_name(self):
        return self.__owner.name

    def show_info(self, is_show_owner=True):
        print(
            f"""
                面积: {str(self.__area)} 平方米,
                价格: {str(self.__price)} 平方米,
                窗户: {"有" if self.__has_window else "没有"}
                卫生间: {self.__has_bathroom}
                厨房: {"有" if self.__has_kitchen else "没有"}
                地址: {self.__address}
                房东: {self.get_owner_name() if is_show_owner else "****"}
            """
        )


class HousingAgency:
    """房屋中介"""

    def __init__(self, name):
        self.__house_infos = []
        self.__name = name

    @property
    def name(self):
        return self.__name

    def add_house_info(self, house_info):
        self.__house_infos.append(house_info)

    def remove_house_info(self, house_info):
        self.__house_infos.remove(house_info)

    def get_search_condition(self, description):
        """将用户描述转化为搜索逻辑"""
        return description

    def get_match_infos(self, search_condition):
        """查找匹配信息"""
        print(f"{self.name,}为您找到以下最适合的房源:")
        for info in self.__house_infos:
            info.show_info(False)
        return self.__house_infos

    def sign_contract(self, house_info: HouseInfo, period):
        """与房东签订协议"""
        print(
            f"{self.name}，与房东：{house_info.owner_name}, 签订{house_info.address}的房子租凭合同，租期{period}年。合同期内{self.name}有权对其进行使用和转租！")

    def sigin_contracts(self, period):
        for info in self.__house_infos:
            self.sigin_contracts(info, period)


class HouseOwner:
    """房东"""

    def __init__(self, name):
        self.__name = None
        self.__house_info = None

        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def house_info(self):
        return self.__house_info

    @house_info.setter
    def house_info(self, house_info):
        self.__house_info = house_info

    def publish_house_info(self, agency: HousingAgency):
        agency.add_house_info(self.house_info)
        print(f"{self.name}在{agency.name}发布租房信息{self.house_info.show_info()}")


class Customer:
    """用户"""

    def __init__(self, name):
        self.__name = None

        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    def find_house(self, description, agency: HousingAgency):
        print(f"我是{self.name}, 我想找一个{description}的房子")
        return agency.get_match_infos(agency.get_search_condition(description))

    def see_house(self, house_infos):
        """去看房"""
        size = len(house_infos)
        return house_infos[size - 1]

    def sign_contract(self, house_info: HouseInfo, agency: HousingAgency, period):
        """与中介签订协议"""
        print(f'{self.name}与中介: {agency.name}签订{house_info.address}的房子租凭合同, 租期: {period}年')


if __name__ == "__main__":
    zz_lian_jia = HousingAgency("zz链家")
    zhangsan = HouseOwner("张三")
    zhangsan.house_info = HouseInfo(20, 2500, 1, "独立卫生间", 0, "上地西里", zhangsan)
    zhangsan.publish_house_info(zz_lian_jia)
    lisi = HouseOwner("李四")
    lisi.house_info = HouseInfo(16, 1800, 1, "公共卫生间", 0, "当代城市家园", lisi)
    lisi.publish_house_info(zz_lian_jia)
    print()

    tony = Customer("Tony")
    house_info = tony.find_house('找个房子', zz_lian_jia)
    appriatehouse = tony.see_house(house_info)
    tony.sign_contract(appriatehouse, zz_lian_jia, 1)
