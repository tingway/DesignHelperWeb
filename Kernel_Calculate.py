import os
import json
import math
import logging
logger = logging.getLogger(__name__)

jsonFilePath = os.path.join(os.getcwd(), "template", f"Json_Contract.json")
with open(jsonFilePath, 'r', encoding='utf-8') as f:
    contractData = json.load(f)

def calKernel(workItemType, workItem):
    print(workItem)
    calDetail = []
    """ 變數列表
    structureType : 側溝、集水井、暗溝、脫管修復
    caseType: 搶修案、一般案
    workType: 新設
    oldType: 無既有設施、矩形溝、U型溝、既有井
    outerFrame: 無、有
    Length: 長度
    WallThick: 壁厚、管壁厚(T)
    Width:淨寬、管徑(D)
    Depth: 淨深、開挖深
    depthRange: 深度範圍
    oldWidth: 既有淨寬、開挖寬(W)
    oldDepth: 既有淨深
    oldWallThick: 既有壁厚

    allWidth: 總寬
    bottomThick210: 結構底板厚
    bottomThick140: 鋪面厚
    bottomThickAll: 結構底板+鋪面厚
    radius: 半圓半徑
    depthDelRadius = Depth-Width/2  # 深度-半圓半徑(方形部分深度)
    outerFrame: 外模

    machineDestroy: 機具拆除
    humanDestroy: 人工拆除
    baseRoadDig: 基礎路幅開挖
    structureDig: 結構開挖
    remaingSoil: 餘方自行處理
    concrete140: 混凝土140
    concreteMain: 混凝土210or 280
    steelFrame: 鋼模
    steelSD280W: 鋼筋SD280"""

    ## 主構造物
    if workItemType == "Main Structure":
        ### 變數設定
        structureType = workItem["structureType"]
        caseType = workItem["caseType"]
        workType = workItem["workType"]
        oldType = workItem["oldType"]
        outerFrame = workItem["outerFrame"]
        Length = float(workItem["Length"])
        WallThick = round(float(workItem["WallThick"]) / 100, 2)
        Width = round(float(workItem["Width"]) / 100, 2)
        Depth = round(float(workItem["Depth"]) / 100, 2)
        oldWidth, oldDepth, oldWallThick = 0, 0, 0
        if workItem["oldWidth"]:
            oldWidth = round(float(workItem["oldWidth"]) / 100, 2)
        if workItem["oldDepth"]:
            oldDepth = round(float(workItem["oldDepth"]) / 100, 2)
            oldWallThick = round(float(workItem["oldWallThick"]) / 100, 2)

        ### 衍生變數設定
        allWidth = round(Width+WallThick*2, 2)
        radius = round(Width/2, 2)
        depthDelRadius = round(Depth-Width/2, 2)  # 深度-半圓半徑(方形部分深度)
        netLength = round(Length-2*WallThick, 2)
        oldNetLength = round(1-2*oldWallThick, 2)
        oldAllWidth = round(oldWidth+oldWallThick*2, 2)
        oldRadius = round(oldWidth/2, 2)
        oldDepthDelRadius = round(oldDepth-oldWidth/2, 2)

        ### 公式字串
        machineDestroy_txt, humanDestroy_txt, baseRoadDig_txt, structureDig_txt, remaingSoil_txt = "", "", "", "", ""
        concrete140_txt, concreteMain_txt, steelFrame_txt, steelSD280W_txt = "", "", "", ""
        asphaltConcrete_txt = ""
        ### 機拆人拆用 (舊總體積)-(舊鏤空部份)，基地路幅開挖用 (新總體積)-(舊總體積),
        ### 餘方用 (新總體積)-(舊鏤空部份)，混凝土用 (新總體積)-(新鏤空部份)

        if structureType == "側溝" or structureType == "暗溝":
            bottomThick210 = 0.2
            bottomThick140 = 0.05
            bottomThickAll = bottomThick210 + bottomThick140
            ### 計算重要項目
            newAllVolumn = f"{allWidth}*({Depth}+{bottomThickAll})"
            oldAllVolumn = f"{oldAllWidth}*({oldDepth}+{bottomThickAll})"
            newHollow = f"{depthDelRadius:.2f}*{Width}-({radius}**2)*3.14*0.5"
            oldHollow = f"{oldDepthDelRadius:.2f}*{oldWidth}-({oldRadius}**2)*3.14*0.5"
            concreteAllVolumn = f"{allWidth}*({Depth}+{bottomThick210})"

            if caseType == "搶修案":
                if workType == "新設":
                    remaingSoil_txt = newAllVolumn
                    concreteMain_txt = concreteAllVolumn + "-" + newHollow
                elif workType == "更新":
                    remaingSoil_txt = newAllVolumn + "-" + newHollow
                    concreteMain_txt = concreteAllVolumn + "-" + newHollow
            elif caseType == "一般案":
                if workType == "新設":
                    baseRoadDig_txt = "( "+ newAllVolumn +" )*0.8"
                    remaingSoil_txt = newAllVolumn
                    concreteMain_txt = concreteAllVolumn + "-" + newHollow
                elif workType == "更新":
                    if  oldType == "矩形溝":
                        oldHollow = f"{oldWidth}*{oldDepth}"
                    if  oldType == "無既有設施":
                        oldAllWidth = allWidth
                        oldAllVolumn = newAllVolumn
                        oldHollow = newHollow
                        oldDepth = Depth
                    machineDestroy_txt = "( " + oldAllVolumn + "-" + oldHollow + " )*0.8"
                    baseRoadDig_txt = "( "+ newAllVolumn + "-" + oldAllVolumn + " )*0.8"
                    if allWidth == oldAllWidth:
                        baseRoadDig_txt = f"( {allWidth}*({Depth}-{oldDepth}) )*0.8"
                    if allWidth == oldAllWidth and Depth == oldDepth:
                        baseRoadDig_txt = ""
                    remaingSoil_txt = newAllVolumn + "-" + oldHollow
                    concreteMain_txt = concreteAllVolumn + "-" + newHollow
            if machineDestroy_txt:
                humanDestroy_txt = machineDestroy_txt[:-1] + "2"
            if baseRoadDig_txt:
                structureDig_txt = baseRoadDig_txt[:-1] + "2"

            if outerFrame == "無":
                # concreteMain_txt = f"({allWidth}*({Depth}+{bottomThick210})-({depthDelRadius:.2f}*{Width})-(({radius}**2)*3.14*0.5))*1.05"
                concreteMain_txt = "(" + concreteMain_txt + ")*1.05"
            # elif outerFrame == "有":
                # concreteMain_txt = f"({allWidth}*({Depth}+{bottomThick210})-({depthDelRadius:.2f}*{Width})-(({radius}**2)*3.14*0.5))"

            concrete140_txt = f"({Width}+{WallThick}+{WallThick})*{bottomThick140}"
            if Depth <= 0.8:
                steelFrame_txt = "1"
            elif Depth > 0.8:
                steelFrame_txt = f"({depthDelRadius:.2f}*2)+({Width}*3.14*0.5)"
            if  oldType == "矩形溝":
                steelFrame_txt = f"({Depth}*2)"
            if structureType == "側溝":
                N_steelD10 = round((Width*100+30)/25,0)+1+round((Depth*100+10)/25,0)*2
                steelSD280W_txt = f"{round((Depth*2+allWidth+0.1)*7*0.994, 2)}+{round(1*N_steelD10*0.56, 2)}"
            elif structureType == "暗溝":
                N_steelD13 = round((Width*100+30)/15,0)+1+round((Depth*100+10)/15,0)*2
                steelSD280W_txt = f"{round((Depth*2+allWidth+0.8)*7*1.56, 2)}+{round(1*N_steelD13*0.994, 2)}"

        elif structureType == "集水井":
            bottomThick210 = 0.15
            bottomThick140 = 0.05
            oldBottomThick210 = {"U型溝":0.2,"矩形溝":0.2,"既有井":0.15,"無既有設施":0.2}[oldType]
            bottomThickAll = bottomThick210 + bottomThick140
            oldBottomThickAll = oldBottomThick210 + bottomThick140
            ### 計算重要項目
            newAllVolumn = f"{allWidth}*({Depth}+{bottomThickAll})*({netLength:.2f}+{WallThick*2})"
            oldAllVolumn = f"{oldAllWidth}*({oldDepth}+{oldBottomThickAll})"
            newHollow = f"({Width}*{netLength:.2f}*{Depth})"
            oldHollow = f"{oldWidth}*{netLength:.2f}*{oldDepth}"
            concreteAllVolumn = f"{allWidth}*({Depth}+{bottomThick210})*({netLength:.2f}+{WallThick*2})"

            if caseType == "搶修案":
                if workType == "新設":
                    remaingSoil_txt = newAllVolumn
                    concreteMain_txt = concreteAllVolumn + "-" + newHollow
                elif workType == "更新":
                    remaingSoil_txt = newAllVolumn + "-" + newHollow
                    concreteMain_txt = concreteAllVolumn + "-" + newHollow
            elif caseType == "一般案":
                if workType == "新設":
                    baseRoadDig_txt = "("+ newAllVolumn +")*0.8"
                    remaingSoil_txt = newAllVolumn
                    concreteMain_txt = concreteAllVolumn + "-" + newHollow
                elif workType == "更新":
                    if  oldType == "U型溝":
                        oldHollow = f"({oldDepthDelRadius:.2f}*{oldWidth})-(({oldRadius}**2)*3.14*0.5)"
                    if  oldType == "矩形溝":
                        oldHollow = f"{oldWidth}*{oldDepth}"
                    if  oldType == "無既有設施":
                        oldAllWidth = allWidth
                        oldAllVolumn = newAllVolumn
                        oldHollow = newHollow
                        oldDepth = Depth
                    machineDestroy_txt = "(" + oldAllVolumn + "-" + oldHollow + ")*0.8"
                    baseRoadDig_txt = "("+ newAllVolumn + "-" + oldAllVolumn + ")*0.8"
                    if allWidth == oldAllWidth:
                        baseRoadDig_txt = f"({allWidth}*({Depth}-{oldDepth}))*0.8"
                    if allWidth == oldAllWidth and Depth == oldDepth:
                        baseRoadDig_txt = ""
                    remaingSoil_txt = newAllVolumn + "-" + newHollow
                    concreteMain_txt = concreteAllVolumn + "-" + newHollow
            if machineDestroy_txt:
                humanDestroy_txt = machineDestroy_txt[:-1] + "2"
            if baseRoadDig_txt:
                structureDig_txt = baseRoadDig_txt[:-1] + "2"

            concrete140_txt = f"({Width}+{WallThick}+{WallThick})*{bottomThick140}"
            if outerFrame == "無":
                # concreteMain_txt = f"({allWidth}*({Depth}+{bottomThick210})*({netLength}+{WallThick*2})-({Width}*{netLength}*{Depth}))*1.05"
                concreteMain_txt = "(" + concreteMain_txt + ")*1.05"
            # elif outerFrame == "有":
            #     concreteMain_txt = f"({allWidth}*({Depth}+{bottomThick210})*({netLength}+{WallThick*2})-({Width}*{netLength}*{Depth}))"
            steelFrame_txt = f"({Width}*{Depth})*2+({netLength}*{Depth})*2"
            N_steelD13 = round(((Width*100+WallThick*100*2)-10)/15,0)
            N_steelD10 = round((Depth*100+5)/25)*2
            steelSD280W_txt = f"{round((Depth*2+allWidth)*7*0.994,2)} + {round(1.4*N_steelD13*0.994,2)} + {round(1*N_steelD10*0.56,2)}"

        elif structureType == "鋼筋混凝土管":
            # Length = 開挖長, Depth = 開挖深
            digWidth = oldWidth # 開挖寬
            diameter = Width    # 管徑
            tubeWallThick = float(workItem["WallThick"])/100    # 管壁厚
            remaingSoil_txt = f"({digWidth}*{Length}*{Depth})-(({diameter}/2+{tubeWallThick:.3f})**2*3.14)"
            concrete140_txt = f"({digWidth}*{Length}*({Depth}-0.2))-(({diameter}/2+{tubeWallThick:.3f})**2*3.14)"
            steelFrame_txt = f"0.5*(3.14*({diameter}+{tubeWallThick:.3f}*2))"
            N_steelD10 = round(Length/0.1,0)
            steelSD280W_txt = f"{round((diameter*2+WallThick*4+0.4)*N_steelD10*0.559, 2)}+{round((Length-0.1)*2*0.559, 2)}"
            asphaltConcrete_txt = f"({digWidth}*{Length})*0.2"

        """合約項目
        1.38 機械拆除
        1.26 人工拆除
        1.31 基地路幅開挖
        1.43 構造物開挖
        1.60 餘方自行處理
        1.99 結構用混凝土140kgf/cm2
        1.102 結構用混凝土210kgf/cm2
        1.137 鋼製模板
        1.156 鋼筋SD280W
        1.168 (免拆模板，鋼質)，厚3mm鋼模
        1.403 瀝青混凝土舖面
        """
        contractInx = ["1.38", "1.26", "1.31", "1.43", "1.60", "1.99", "1.102", "1.137", "1.156"]
        itemTxtList = [machineDestroy_txt, humanDestroy_txt, baseRoadDig_txt, structureDig_txt, remaingSoil_txt,
                       concrete140_txt, concreteMain_txt, steelFrame_txt, steelSD280W_txt]
        if structureType == "側溝" or structureType == "暗溝":
            inx_concreteMain = contractInx.index("1.102")
            inx_steelFrame = contractInx.index("1.137")
            if WallThick < 0.2:
                contractInx[inx_concreteMain] = "1.105"    # 結構用混凝土，預拌，280kgf/cm2
            if Depth <= 0.8:
                if Width < 0.45:
                    contractInx[inx_steelFrame] = "1.137"    #鋼製模板，U型溝用，W=40cm，L=120cm.
                elif 0.45 <= Width < 0.65:
                    contractInx[inx_steelFrame] = "1.139"    #鋼製模板，U型溝用，W=50cm，L=120cm.
                elif Width >= 0.65:
                    contractInx[inx_steelFrame] = "1.141"    #鋼製模板，U型溝用，W=60cm，L=120cm.
            elif Depth > 0.8:
                if Width < 0.45:
                    contractInx[inx_steelFrame] = "1.138"    #鋼製模板，U型溝用，W=40cm，L=120cm，H>80cm.
                elif 0.45 <= Width < 0.65:
                    contractInx[inx_steelFrame] = "1.140"    #鋼製模板，U型溝用，W=50cm，L=120cm，H>80cm.
                elif Width >= 0.65:
                    contractInx[inx_steelFrame] = "1.142"    #鋼製模板，U型溝用，W=60cm，L=120cm，H>80cm.
            if  oldType == "矩形溝":
                contractInx[inx_steelFrame] = "1.124"        #場鑄結構混凝土用模板，清水模板，丙種.

        if structureType == "集水井":
            inx_steelFrame = contractInx.index("1.137")
            contractInx[inx_steelFrame] = "1.124"    #場鑄結構混凝土用模板，清水模板，丙種.

        if structureType == "鋼筋混凝土管":
            contractInx = ["1.60","1.99", "1.168", "1.156", "1.403"]
            itemTxtList = [remaingSoil_txt, concrete140_txt, steelFrame_txt, steelSD280W_txt, asphaltConcrete_txt]

        contractInx = [contractInx[inx] for inx, item in enumerate(itemTxtList) if item]
        itemValList = [round(eval(item)+1e-12,3) for item in itemTxtList if item]
        itemTxtList = [item for item in itemTxtList if item]

        for item in itemTxtList:
            if "**" in item:
                inx = itemTxtList.index(item)
                itemTxtList[inx] = item.replace("**","^")

        for i in range(len(contractInx)):
            calDetail.append([contractInx[i], contractData[contractInx[i]][0], "=", f"{itemValList[i]:.3f}", contractData[contractInx[i]][1]] )
            calDetail.append(["", itemTxtList[i], "", "", ""])

    ## 頂板
    elif workItemType == "Cover Structure":
        structureType = workItem["structureType"]
        caseType = workItem["caseType"]
        workType = workItem["workType"]
        coverType = workItem["coverType"]
        Length = float(workItem["Length"])
        coverWidth = round(float(workItem["coverWidth"]) / 100, 2)
        coverThick = {"13cm":0.13, "15cm":0.15, "5cm":0.05, "10cm":0.1}[workItem["coverThick"]]
        grilleWidth = {"45cm":0.45, "55cm":0.55, "65cm":0.65}[workItem["grilleWidth"]]
        grilleType = workItem["grilleType"]

        machineDestroy_txt, humanDestroy_txt, baseRoadDig_txt, structureDig_txt, remaingSoil_txt,  = "", "", "", "", ""
        concreteMain_txt, steelSD280W_txt, steelFrame_txt, wireTube_txt, grilleAndFrame_txt, normalFrame_txt = "", "", "", "", "", ""
        asphaltStickLayer_txt, asphaltConcrete95_txt, asphaltConcrete190_txt = "", "", ""

        if structureType == "側溝頂板" or structureType == "集水井頂板":
            if caseType == "一般案":
                if workType == "更新":
                    machineDestroy_txt = {"S1":f"({coverWidth}*{coverThick})*0.8",
                                          "S2":f"({coverWidth}*{coverThick}-{grilleWidth}*0.65*{coverThick})*0.8",
                                          "L1":f"({coverWidth}*{coverThick}+(0.15+0.18)*0.15/2)*0.8",
                                          "L2":f"({coverWidth}*{coverThick}+(0.15+0.18)*0.15/2-{grilleWidth}*0.65*{coverThick})*0.8"}[coverType]  # 多加墩座
                elif workType == "新設":
                    baseRoadDig_txt = {"S1":f"({coverWidth}*{coverThick})*0.8",
                                       "S2":f"({coverWidth}*{coverThick})*0.8",
                                       "L1":f"({coverWidth}*{coverThick}+(0.15+0.18)*0.15/2)*0.8",
                                       "L2":f"({coverWidth}*{coverThick}+(0.15+0.18)*0.15/2)*0.8"}[coverType] # 多加墩座
            if workType == "更新":
                remaingSoil_txt = {"S1":f"{coverWidth}*{coverThick}",
                                "S2":f"{coverWidth}*{coverThick}-{grilleWidth}*0.65*{coverThick}",
                                "L1":f"({coverWidth}*{coverThick}+(0.15+0.18)*0.15/2)",
                                "L2":f"({coverWidth}*{coverThick}+(0.15+0.18)*0.15/2)-{grilleWidth}*0.65*{coverThick}"}[coverType] # 多加墩座
                concreteMain_txt = {"S1":f"{coverWidth}*{coverThick}",
                                "S2":f"{coverWidth}*{coverThick}-{grilleWidth}*0.65*{coverThick}",
                                "L1":f"({coverWidth}*{coverThick}+(0.15+0.18)*0.15/2)",
                                "L2":f"({coverWidth}*{coverThick}+(0.15+0.18)*0.15/2)-{grilleWidth}*0.65*{coverThick}"}[coverType]
            elif workType == "新設":
                remaingSoil_txt = {"S1":f"{coverWidth}*{coverThick}",
                                "S2":f"{coverWidth}*{coverThick}",
                                "L1":f"({coverWidth}*{coverThick}+(0.15+0.18)*0.15/2)",
                                "L2":f"({coverWidth}*{coverThick}+(0.15+0.18)*0.15/2)"}[coverType] # 多加墩座
                concreteMain_txt = {"S1":f"{coverWidth}*{coverThick}",
                                "S2":f"{coverWidth}*{coverThick}-{grilleWidth}*0.65*{coverThick}",
                                "L1":f"({coverWidth}*{coverThick}+(0.15+0.18)*0.15/2)",
                                "L2":f"({coverWidth}*{coverThick}+(0.15+0.18)*0.15/2)-{grilleWidth}*0.65*{coverThick}"}[coverType]
            if coverThick == 0.13:
                steelSD280W_txt = {"S1":f"{(coverWidth-0.1)*0.994*10+4.97:.2f}",
                                "S2":f"{((coverWidth-grilleWidth+0.05)-0.08-0.12)*13*0.994+2.49*2+5.57:.2f}+0.45",
                                "L1":f"{(coverWidth-0.1)*0.994*10+4.97+3.22+2.06:.2f}",
                                "L2":f"{((coverWidth-grilleWidth+0.05)-0.08-0.12)*13*0.994+2.49*2+5.57+3.22+2.49:.2f}+0.45"}[coverType]
            elif coverThick == 0.15:
                steelSD280W_txt = {"S1":f"{((coverWidth-0.06)*2+0.1*3)*8*0.994+9.94:.2f}",
                                "S2":f"{(((coverWidth-grilleWidth+0.05)-0.026-0.066)*2+(0.065*3)*2)*13*0.56+0.39:.2f}+{7.36*2+11.13:.2f}",
                                "L1":f"{((coverWidth-0.06)*2+0.1*3)*8*0.994+9.94+4.02+2.06:.2f}",
                                "L2":f"{(((coverWidth-grilleWidth+0.05)-0.026-0.066)*2+(0.065*3)*2)*13*0.56+0.39:.2f}+{7.36*2+11.13+3.92+2.49:.2f}"}[coverType]
            if coverType in ["S1", "L1"]:
                steelFrame_txt = f"{round(coverWidth-0.2,2)}*1"
                wireTube_txt = f"{coverThick+0.02:.2f}"
            elif coverType in ["S2", "L2"]:
                steelFrame_txt = f"{round(coverWidth-0.2,2)}*1-{grilleWidth}*0.65"
                grilleAndFrame_txt = f"1"
            normalFrame_txt = {"S1":f"1*{coverThick}",
                            "S2":f"({grilleWidth}+0.65)*{coverThick}*2+1*{coverThick}",
                            "L1":f"1*{coverThick}*2",
                            "L2":f"({grilleWidth}+0.65)*{coverThick}*2+1*{coverThick}*2"}[coverType]

        elif structureType == "暗溝頂板":
            if caseType == "一般案":
                if workType == "更新":
                    machineDestroy_txt = f"({coverWidth}*(0.2+{coverThick}))*0.8"
                elif workType == "新設":
                    baseRoadDig_txt = f"({coverWidth}*(0.2+{coverThick}))*0.8"
            remaingSoil_txt = f"{coverWidth}*(0.2+{coverThick})"
            concreteMain_txt = f"{coverWidth}*0.2"
            steelSD280W_txt = f"{(coverWidth-0.1)*0.994*10+4.97:.2f}"
            N_steelD13 = (round(coverWidth*100/15,0)+1)*2
            steelSD280W_txt = f"{round((coverWidth+0.1)*16*0.994, 2)}+{round(1*N_steelD13*0.994, 2)}"
            steelFrame_txt = f"{round(coverWidth-0.2,2)}*1"
            if coverThick == 0.05:
                asphaltStickLayer_txt = f"{coverWidth}*1"
            elif coverThick == 0.1:
                asphaltStickLayer_txt = f"{coverWidth}*1*2"
                asphaltConcrete190_txt = f"{coverWidth}*0.05"
            asphaltConcrete95_txt = f"{coverWidth}*0.05"

        # 機拆->人拆, 基地路幅開挖->結構物開挖
        if machineDestroy_txt:
            humanDestroy_txt = machineDestroy_txt[:-1] + "2"
        if baseRoadDig_txt:
            structureDig_txt = baseRoadDig_txt[:-1] + "2"

        contractInx = ["1.38",  # 機械拆除
                       "1.26",  # 人工拆除
                       "1.31",  # 基地路幅開挖
                       "1.43",  # 構造物開挖
                       "1.60",  # 餘方自行處理
                       "1.105", # 結構用混凝土280kgf/cm2
                       "1.168", # 鋼模
                       "1.156", # 鋼筋SD280W
                       "1.320", # 導管
                       "1.276", # 鍍鋅格柵及框座
                       "1.129", # 場鑄結構混凝土用模板，普通模板，丙種
                       "1.71",  # 瀝青黏層，快凝油溶瀝青，RC-70
                       "1.74",  # 瀝青混凝土舖面，粗粒料9.5mm，黏度AC(1)-20，零星工程
                       "1.77"   # 瀝青混凝土舖面，粗粒料19.0mm，黏度AC(1)-20，零星工程
                       ]
        itemTxtList = [machineDestroy_txt, humanDestroy_txt, baseRoadDig_txt, structureDig_txt, remaingSoil_txt, concreteMain_txt,
                    steelFrame_txt, steelSD280W_txt, wireTube_txt, grilleAndFrame_txt, normalFrame_txt,
                    asphaltStickLayer_txt, asphaltConcrete95_txt, asphaltConcrete190_txt]

        contractInx = [contractInx[inx] for inx, item in enumerate(itemTxtList) if item]
        itemValList = [round(eval(item)+1e-12,3) for item in itemTxtList if item]
        itemTxtList = [item for item in itemTxtList if item]

        if coverType in ["S2", "L2"]:
            inx_grille = contractInx.index("1.276")
            contractInx[inx_grille] = {0.45:"1.276", 0.55:"1.277", 0.65:"1.278"}[grilleWidth]
            if grilleType == "細目型":
                contractInx[inx_grille] = {0.45:"1.280", 0.55:"1.281", 0.65:"1.282"}[grilleWidth]

        for i in range(len(contractInx)):
            calDetail.append([contractInx[i], contractData[contractInx[i]][0], "=", f"{itemValList[i]:.3f}", contractData[contractInx[i]][1]] )
            calDetail.append(["", itemTxtList[i], "", "", ""])

    ## 復舊
    elif workItemType == "Recover":
        Thick = {"13cm":0.13, "15cm":0.15, "5cm":0.05, "10cm":0.1}[workItem["Thick"]]
        Length_Formula = workItem["Length"]
        Width = round(float(workItem["Width"]) / 100, 2)
        lineMark = workItem["lineMark"]
        lineMarkFormulas = workItem["lineMarkFormulas"]

        remaingSoil_txt = ""        # 1.60 餘方自行處理
        asphaltRemove407_txt = ""      # 1.407 瀝青混凝土面層刨除，刨除機1.2m寬，緊急搶修工程用，未含刨除料運費
        asphaltRemove90_txt = ""      # 1.90 瀝青混凝土面層刨除，厚5cm，刨除機1.2m寬，未含運費
        asphaltRemove93_txt = ""      # 1.93 瀝青混凝土面層刨除，厚10cm，刨除機1.2m寬，未含運費
        asphaltShipping147_txt = ""    # 1.47 瀝青混凝土面層刨除，刨除料運費
        asphaltRolling398_txt = ""     # 1.398 瀝青混凝土舖面，舖築及滾壓，緊急搶修工程用，鋪設面積≦50m2適用
        asphaltRolling399_txt = ""     # 1.399 瀝青混凝土舖面，舖築及滾壓，緊急搶修工程用，鋪設面積＞50m2適用
        asphaltRemove403_txt = ""      # 1.403 瀝青混凝土舖面，粗粒料9.5mm，針入度60~70，緊急搶修工程用，舖築及滾壓另計
        asphaltRemove402_txt = ""      # 1.402 瀝青混凝土舖面，粗粒料19.0mm，針入度60~70，緊急搶修工程用，舖築及滾壓另計
        asphaltRemove405_txt = ""      # 1.405 瀝青混凝土面，再生粒料，粗粒料9.5mm，緊急搶修工程用，舖築及滾壓另計
        asphaltRemove404_txt = ""      # 1.404 瀝青混凝土面，再生粒料，粗粒料19.0mm，緊急搶修工程用，舖築及滾壓另計
        asphaltRemove406_txt = ""      # 1.406 瀝青混凝土面，密級配改質瀝青混凝土，粗粒料19mm，改質Ⅲ型，緊急搶修工程用，舖築及滾壓另計
        asphaltGrass74_txt = ""       # 1.74 瀝青混凝土舖面，粗粒料9.5mm，黏度AC(1)-20，零星工程用
        asphaltGrass77_txt = ""       # 1.77 瀝青混凝土舖面，粗粒料19.0mm，黏度AC(1)-20，零星工程用
        asphalt184_txt = ""         # 1.84 再生瀝青混凝土鋪面，(密級配，30%回收料)，粗粒料9.5mm，零星工程用
        asphalt187_txt = ""         # 1.87 再生瀝青混凝土鋪面，(密級配，30%回收料)，粗粒料19.0mm，零星工程用
        asphalt180_txt = ""         # 1.80 密級配改質瀝青混凝土，粗粒料19mm，改質Ⅲ型，零星工程用
        asphalt189_txt = ""         # 1.89 瀝青混凝土路面，樹脂混凝土，路面修補
        asphaltStickLayer71_txt = ""  # 1.71 瀝青黏層，快凝油溶瀝青，RC-70
        asphalt1379_txt = ""        # 1.379 搬運費
        asphalt118_txt = ""         # 1.18 開挖機
        asphalt11_txt = ""          # 1.1 操作手

        if workItem["recoverType"] == "路面切割":
            if workItem["materialType"] == "樹脂混凝土":
                lineMarkFirstRow = 2
                remaingSoil_txt = f"{Length_Formula}*{Width}*{Thick}"
                asphalt189_txt = f"{Length_Formula}*{Width}*{Thick}"
            elif workItem["materialType"] == "AC回填":
                lineMarkFirstRow = 3
                remaingSoil_txt = f"{Length_Formula}*{Width}*{Thick}"
                asphaltStickLayer71_txt = f"{Length_Formula}*{Width}"
                asphaltGrass74_txt = f"{Length_Formula}*{Width}*{Thick}"

        elif workItem["recoverType"] == "道路銑鋪":
            recoverArea = eval(Length_Formula)
            if workItem["caseType"] == "一般案":
                lineMarkFirstRow = 7
                if Thick == 0.05:
                    asphaltRemove90_txt = f"{Length_Formula}"
                    asphaltStickLayer71_txt = f"{Length_Formula}"
                elif Thick == 0.1:
                    asphaltRemove93_txt = f"{Length_Formula}"
                    asphaltStickLayer71_txt = f"({Length_Formula})*2"
                if workItem["materialType"] == "一般瀝青":
                    asphaltGrass74_txt = f"({Length_Formula})*0.05"
                    if Thick == 0.1:
                        lineMarkFirstRow = 8
                        asphaltGrass77_txt = f"({Length_Formula})*0.05"
                elif workItem["materialType"] == "再生瀝青":
                    asphalt184_txt = f"({Length_Formula})*0.05"
                    if Thick == 0.1:
                        lineMarkFirstRow = 8
                        asphalt187_txt = f"({Length_Formula})*0.05"
                elif workItem["materialType"] == "改質瀝青":
                    asphalt180_txt = f"{Length_Formula}*{Thick}"

            elif workItem["caseType"] == "搶修案":
                lineMarkFirstRow = 8
                if recoverArea > 50:
                    asphaltRolling399_txt = "1"
                else:
                    asphaltRolling398_txt = "1"
                if Thick == 0.05:
                    asphaltRemove407_txt = "1"
                    asphaltStickLayer71_txt = f"{Length_Formula}"
                elif Thick == 0.1:
                    asphaltRemove407_txt = "1"
                    asphaltStickLayer71_txt = f"({Length_Formula})*2"
                if workItem["materialType"] == "一般瀝青":
                    asphaltRemove403_txt = f"({Length_Formula})*0.05"
                    if Thick == 0.1:
                        lineMarkFirstRow = 9
                        asphaltRemove402_txt = f"({Length_Formula})*0.05"
                elif workItem["materialType"] == "再生瀝青":
                    asphaltRemove405_txt = f"({Length_Formula})*0.05"
                    if Thick == 0.1:
                        lineMarkFirstRow = 9
                        asphaltRemove404_txt = f"({Length_Formula})*0.05"
                elif workItem["materialType"] == "改質瀝青":
                    asphaltRemove406_txt = f"{Length_Formula}*{Thick}"

            asphaltShipping147_txt = f"({Length_Formula})*{Thick}"
            asphalt1379_txt = "1"        # 1.379 搬運費
            asphalt118_txt = "1"         # 1.18 開挖機
            asphalt11_txt = "1"          # 1.1 操作手
            if recoverArea > 200:
                val = 1+(recoverArea-200)//200
                asphalt118_txt = f"{val}"
                asphalt11_txt = f"{val}"

        contractInx = ["1.60",  # 餘方自行處理
                       "1.407",   # 瀝青混凝土面層刨除，刨除機1.2m寬，緊急搶修工程用，未含刨除料運費
                       "1.90",  # 瀝青混凝土面層刨除，厚5cm，刨除機1.2m寬，未含運費
                       "1.93",  # 瀝青混凝土面層刨除，厚10cm，刨除機1.2m寬，未含運費

                       "1.47",  # 瀝青混凝土面層刨除，刨除料運費
                       "1.398",  # 瀝青混凝土舖面，舖築及滾壓，緊急搶修工程用，鋪設面積≦50m2適用
                       "1.399",  # 瀝青混凝土舖面，舖築及滾壓，緊急搶修工程用，鋪設面積≦50m2適用
                       "1.71",  # 瀝青黏層，快凝油溶瀝青，RC-70

                       "1.403",  # 瀝青混凝土舖面，粗粒料9.5mm，針入度60~70，緊急搶修工程用，舖築及滾壓另計
                       "1.402",  # 瀝青混凝土舖面，粗粒料19.0mm，針入度60~70，緊急搶修工程用，舖築及滾壓另計
                       "1.405",  # 瀝青混凝土面，再生粒料，粗粒料9.5mm，緊急搶修工程用，舖築及滾壓另計
                       "1.404",  # 瀝青混凝土面，再生粒料，粗粒料19.0mm，緊急搶修工程用，舖築及滾壓另計
                       "1.406",  # 瀝青混凝土面，密級配改質瀝青混凝土，粗粒料19mm，改質Ⅲ型，緊急搶修工程用，舖築及滾壓另計

                       "1.74",  # 瀝青混凝土舖面，粗粒料9.5mm，黏度AC(1)-20，零星工程用
                       "1.77",  # 瀝青混凝土舖面，粗粒料19.0mm，黏度AC(1)-20，零星工程用
                       "1.84",  # 再生瀝青混凝土鋪面，(密級配，30%回收料)，粗粒料9.5mm，零星工程用
                       "1.87",  # 再生瀝青混凝土鋪面，(密級配，30%回收料)，粗粒料19.0mm，零星工程用
                       "1.80",  # 密級配改質瀝青混凝土，粗粒料19mm，改質Ⅲ型，零星工程用
                       "1.89",  # 瀝青混凝土路面，樹脂混凝土，路面修補

                       "1.379", # 搬運費，AC施工機械(面積2000m2以下適用)
                       "1.18",  # 開挖機，0.70-0.79m3
                       "1.1",   # 操作手，重機械
                       ]
        itemTxtList = [remaingSoil_txt, asphaltRemove407_txt, asphaltRemove90_txt, asphaltRemove93_txt,
                       asphaltShipping147_txt, asphaltRolling398_txt, asphaltRolling399_txt, asphaltStickLayer71_txt,
                       asphaltRemove403_txt, asphaltRemove402_txt, asphaltRemove405_txt, asphaltRemove404_txt, asphaltRemove406_txt,
                       asphaltGrass74_txt, asphaltGrass77_txt, asphalt184_txt, asphalt187_txt, asphalt180_txt, asphalt189_txt,
                       asphalt1379_txt, asphalt118_txt, asphalt11_txt]

        contractInx = [contractInx[inx] for inx, item in enumerate(itemTxtList) if item]
        itemValList = [round(eval(item)+1e-12,3) for item in itemTxtList if item]
        itemTxtList = [item for item in itemTxtList if item]

        rowCount = len(contractInx)
        lineMarkFormulasSum = 0
        if lineMark and len(lineMark) > 0:
            contractInx.append("1.448")
            rowCount = len(contractInx) + len(lineMark)-1
            lineMarkFormulasSum = "+".join(lineMarkFormulas)
            firstRow = "+"
            if len(lineMark) == 1:
                firstRow = ""

            for i in range(rowCount):
                if i < lineMarkFirstRow:
                    calDetail.append([contractInx[i], contractData[contractInx[i]][0], "=", f"{itemValList[i]:.3f}", contractData[contractInx[i]][1]] )
                    calDetail.append(["", itemTxtList[i], "", "", ""])
                elif i == lineMarkFirstRow:
                    calDetail.append([contractInx[i], contractData[contractInx[i]][0], "=", f"{eval(lineMarkFormulasSum):.3f}", contractData[contractInx[i]][1]] )
                    calDetail.append(["", lineMarkFormulas[0]+firstRow, "", lineMark[0], ""])
                elif i == (rowCount-1):
                    calDetail.append(["", lineMarkFormulas[i-len(contractInx)+1], "", lineMark[i-len(contractInx)+1], ""])
                else:
                    calDetail.append(["", lineMarkFormulas[i-len(contractInx)+1]+"+", "", lineMark[i-len(contractInx)+1], ""])
        else:
            for i in range(len(contractInx)):
                calDetail.append([contractInx[i], contractData[contractInx[i]][0], "=", f"{itemValList[i]:.3f}", contractData[contractInx[i]][1]] )
                calDetail.append(["", itemTxtList[i], "", "", ""])
        if workItem.get("colorCover"):
                val = f"{eval(workItem['colorCover']):.3f}"
                calDetail.append(["1.441", contractData["1.441"][0], "=", val, contractData["1.441"][1]] )
                calDetail.append(["", workItem['colorCover'], "", "", ""])

    ## 其他
    elif workItemType == "Others":
        # inx = ['1.1', '1.3', '1.4', '1.11', '1.16',
        #         '1.19', "1.97", '1.333', '1.335', '1.364',
        #         '1.366', '1.387', '1.396', '1.421', '1.429',
        #         '1.432', '1.433']
        # expectWorkingDay = int(workItem["expectWorkingDay"])
        for key in workItem.keys():
            if key == "expectWorkingDay" or key == "workItemType":
                continue
            else:
                txt = f"{workItem[key]}"

            ## replace "^" by "**"
            if "^" in txt:
                txt.replace("^", "**")

            try:
                calDetail.append([key, contractData[key][0], "=", f"{eval(txt):.3f}", contractData[key][1]])
                if "**" in txt:
                    txt.replace("**", "^")
                calDetail.append(["", txt, "", "", ""])
            except:
                txt = f"error at :{key}{contractData[key][0]}"
                logger.info(txt)

    return(calDetail)

# 供 app 使用的別名
calDetail = calKernel