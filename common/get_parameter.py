# coding:utf-8
import xlrd


class Data(object):

    def __init__(self, filepath, sheetname):
        self.data = xlrd.open_workbook(filepath)
        self.table = self.data.sheet_by_name(sheetname)
        # 获取第一行作为key值
        self.keys = self.table.row_values(0)
        # 获取总行数
        self.rowNum = self.table.nrows
        # 获取总列数
        self.colNum = self.table.ncols

    def get_data(self):
        parameters_dict = []
        keys = []
        for i in range(self.rowNum - 1):
            # 获取除开第一行的
            i += 1
            parameters_keys = self.keys
            parameters = self.table.row_values(i)
            # num = self.table.col_values(1)
            para = dict(zip(parameters_keys, parameters))
            parameters_dict.append(para)
        for i in range(len(parameters_dict)):
            i += 1
            keys.append(i)
        paras = dict(zip(keys, parameters_dict))
        return paras


if __name__ == "__main__":
    filePath = "F:\web-autotest\datas\one.xls"
    sheetName = "Sheet1"
    d = Data(filePath, sheetName)
    d1 = d.get_data()
    print(d1[5]["适用车型"])
