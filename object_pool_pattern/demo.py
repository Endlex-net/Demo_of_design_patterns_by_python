from abc import ABC, abstractmethod


class Reusable(ABC):
    """可以重复使用的对象"""

    def __init__(self):
        self.pool: ReusabletPool = None

    def release(self):
        self.pool.release(self)


class ReusabletPool(ABC):
    """对象池"""

    def __init__(self, size: int):
        self.max_size = size
        self._reusables = []
        for _ in range(size):
            reusbale = self._create_object()
            reusbale.pool = self
            self._reusables.append(reusbale)

    @abstractmethod
    def _create_object(self) -> Reusable:
        """创建对象"""
        pass

    def acquire(self):
        return self._reusables.pop()

    def release(self, reusable):
        self._reusables.append(reusable)


class MySqlClient(Reusable):
    """MySql连接"""

    def __init__(self):
        super().__init__()
        print("打开了一个和数据库的连接")

    def select(self):
        """查询"""
        print("查询了一条sql查询")


class MySqlClientPool(ReusabletPool):
    """Mysql连接池"""

    def _create_object(self):
        return MySqlClient()


if __name__ == "__main__":
    mysql_client_pool = MySqlClientPool(10)

    mysql_client = mysql_client_pool.acquire()
    mysql_client.select()
    mysql_client.release()
