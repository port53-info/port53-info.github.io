---
title: TEST
date: 2023-11-01
---

import * as echarts from 'echarts/core';
import {
  ToolboxComponent,
  TooltipComponent,
  GridComponent,
  LegendComponent
} from 'echarts/components';
import { BarChart, LineChart } from 'echarts/charts';
import { UniversalTransition } from 'echarts/features';
import { CanvasRenderer } from 'echarts/renderers';
const colors = ['#5470C6', '#91CC75', '#EE6666'];
const dot = [
  ['2021-12', 7833, 2247],
  ['2022-01', 10440, 2484],
  ['2022-02', 10554, 2493],
  ['2022-03', 10843, 2472],
  ['2022-04', 9928, 2508],
  ['2022-05', 9401, 2535],
  ['2022-06', 9325, 2578],
  ['2022-07', 9623, 2907],
  ['2022-08', 9260, 2750],
  ['2022-09', 8914, 2544],
  ['2022-10', 9200, 2579],
  ['2022-11', 10706, 2885],
  ['2022-12', 10102, 2759],
  ['2023-01', 9773, 2658],
  ['2023-02', 9494, 2559],
  ['2023-03', 9224, 2457],
  ['2023-04', 9005, 2415],
  ['2023-10', 16315, 1384]
];
const dot_x = dot.map(function (item) {
  return item[0];
});
const dot_ipcount = dot.map(function (item) {
  return item[1];
});
const dot_adncount = dot.map(function (item) {
  return item[2];
});
//////////
const doh = [
  ['2021-12', 4735, 1005],
  ['2022-01', 6009, 2884],
  ['2022-02', 6441, 3130],
  ['2022-03', 4495, 1245],
  ['2022-04', 5268, 1279],
  ['2022-05', 4819, 1322],
  ['2022-06', 4204, 1355],
  ['2022-07', 4235, 1566],
  ['2022-08', 4154, 1496],
  ['2022-09', 4414, 1519],
  ['2022-10', 4468, 1551],
  ['2022-11', 4685, 1502],
  ['2022-12', 4587, 1413],
  ['2023-01', 4531, 1366],
  ['2023-02', 4481, 1316],
  ['2023-03', 4428, 1279],
  ['2023-04', 4380, 1252],
  ['2023-10', 5205, 571]
];
const doh_x = doh.map(function (item) {
  return item[0];
});
const doh_ipcount = doh.map(function (item) {
  return item[1];
});
const doh_adncount = doh.map(function (item) {
  return item[2];
});

option = {
  color: colors,
  tooltip: {
    trigger: 'axis',
    axisPointer: {
      type: 'cross'
    }
  },
  toolbox: {
    feature: {
      dataView: { show: true, readOnly: false },
      restore: { show: true },
      saveAsImage: { show: true }
    }
  },
  grid: [
    //0 dot
    { x: '7%', y: '7%', height: '35%', left: '10%' },
    //1 doh
    { x: '7%', y2: '7%', height: '35%', left: '10%', bottom: '15%' }
  ],
  xAxis: [
    {
      show: true, //隐藏了x轴
      type: 'category',
      gridIndex: 0, //对应前面grid的索引位置（第一个）
      axisTick: {
        alignWithLabel: true
      },
      data: dot_x
    },
    {
      type: 'category',
      gridIndex: 1, //对应前面grid的索引位置（第二个）
      axisTick: {
        alignWithLabel: true
      },
      data: doh_x
    }
  ],
  yAxis: [
    {
      type: 'value',
      gridIndex: 0, //对应前面grid的索引位置（第二个）
      name: 'dt ip count',
      splitLine: { show: false },
      nameLocation: 'middle',
      nameTextStyle: {
        padding: 25
      },
      position: 'right',
      axisLine: {
        lineStyle: {
          color: colors[0]
        }
      },
      axisLabel: {
        formatter: '{value}'
      }
    },
    {
      type: 'value',
      gridIndex: 0,
      nameLocation: 'middle',
      name: 'dot adn count',
      nameTextStyle: {
        padding: 25
      },
      splitLine: { show: false },
      position: 'left',
      axisLine: {
        lineStyle: {
          color: colors[1]
        }
      },
      axisLabel: {
        formatter: '{value}'
      }
    },
    {
      type: 'value',
      gridIndex: 1,
      name: '平均温度',
      nameTextStyle: {
        padding: 25
      },
      position: 'left',
      nameLocation: 'middle',
      splitLine: { show: false },
      //nameLocation: 'start',//y轴name的位置
      //inverse: true,
      axisLine: {
        lineStyle: {
          //color: '#f8f106'
        }
      },
      axisLabel: {
        formatter: '{value}',
        textStyle: {
          fontSize: 12 //y轴坐标轴上的字体大小
        }
      }
    },
    {
      type: 'value',
      gridIndex: 1,
      name: '测试',
      nameTextStyle: {
        padding: 25
      },
      nameLocation: 'middle',
      position: 'right',
      //nameLocation: 'start',//y轴name的位置
      //inverse: true,
      splitLine: { show: false },
      axisLine: {
        lineStyle: {
          //color: colors[1]
        }
      },
      axisLabel: {
        formatter: '{value}',
        textStyle: {
          fontSize: 12 //y轴坐标轴上的字体大小
        }
      }
    }
  ],
  series: [
    {
      name: '蒸发量',
      // type:'bar',
      // name: "累产气量"
      type: 'bar',
      xAxisIndex: 0,
      yAxisIndex: 2,

      data: dot_ipcount
    },
    {
      name: '降水量',
      type: 'line',
      xAxisIndex: 0,
      yAxisIndex: 3,

      data: dot_adncount
    },
    {
      name: '平均温度',
      type: 'bar',

      xAxisIndex: 1,
      yAxisIndex: 0,

      data: doh_ipcount
    },
    {
      name: '测试',
      type: 'line',
      xAxisIndex: 1,
      yAxisIndex: 1,
      data: doh_adncount
    }
  ]
};
option && myChart.setOption(option);
