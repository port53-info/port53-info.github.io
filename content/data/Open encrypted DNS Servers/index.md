---
title: Open Encrypted DNS Servers
date: 2024-04-20
---

We scan the IPv4 address space for servers supporting DNS-over-TLS (DoT, [RFC 7858](https://datatracker.ietf.org/doc/html/rfc7858)), DNS-over-HTTPS (DoH, [RFC 8484](https://datatracker.ietf.org/doc/html/rfc8484)), DNS-over-QUIC (DoQ, [RFC 9250](https://datatracker.ietf.org/doc/html/rfc9250)), and DoH3.
Here we provide statistics and data about open encrypted DNS servers, including their IP addresses, authentication domain names (ADN), locations, and certificate verification status.

## Related publications

> [WWW '24] **Ruixuan Li**, **Baojun Liu**, **Chaoyi Lu**, **Haixin Duan**, and Jun Shao. A Worldwide View on the Reachability of Encrypted DNS Services. To appear in Proceedings of the Web Conference 2024 <br>
<a class="btn btn-outline-primary btn-page-header" href="https://github.com/lrxgoat/DoE_Reachability/" target="_blank" rel="noopener">Code</a>


> [IMC '19] **Chaoyi Lu**, **Baojun Liu**, Zhou Li, Shuang Hao, **Haixin Duan**, Mingming Zhang, Chunying Leng, Ying Liu, Zaifeng Zhang, and Jianping Wu. An End-to-End, Large-Scale Measurement of DNS-over-Encryption: How Far Have We Come?. In Proceedings of the 2019 ACM Internet Measurement Conference <br>
<a class="btn btn-outline-primary btn-page-header" href="/files/3355369.3355580.pdf" target="_blank" rel="noopener">Paper</a>
<a class="btn btn-outline-primary btn-page-header" href="/files/acm_3355369.3355580.bib" target="_blank" rel="noopener">Bibtex</a>
<a class="btn btn-outline-primary btn-page-header" href="https://www.irtf.org/anrp/" target="_blank" rel="noopener">IRTF Applied Networking Research Prize Recepient</a>


> [ToN '23] **Ruixuan Li**, Xiaofeng Jia, Zhenyong Zhang, Jun Shao, Rongxing Lu, Jingqiang Lin, Xiaoqi Jia, Guiyi Wei. A Longitudinal and Comprehensive Measurement of DNS Strict Privacy. In IEEE/ACM Transactions on Networking <br>
<a class="btn btn-outline-primary btn-page-header" href="/files/A_Longitudinal_and_Comprehensive_Measurement_of_DNS_Strict_Privacy.pdf" target="_blank" rel="noopener">Paper</a>
<a class="btn btn-outline-primary btn-page-header" href="/files/IEEE Xplore Citation BibTeX Download 2023.11.11.4.34.55.bib" target="_blank" rel="noopener">Bibtex</a>

<br>

## Statistics and summary

Our scan is performed monthly.
Data for DoT/DoH dates back to Dec 2021, and DoQ/DoH3 dates back to Jul 2022.

**A) Count of IPs (v4) and ADNs of encrypted DNS servers**

Following an evident growing trend in early stages since proposal, the count of IPs and ADNs associated with each protocol shows small fluctuations in recent years.

<div id="graph_a" style="height: 650%"></div>

<br>
<br>

**B) Validity of certificates**

Invalid certificates, especially self-signed certificates, still pose as a substantial issue for open DoT servers (>30% of all).
The same problem is minor for other protocols.

<div id="graph_b" style="height: 350%"></div>

<!-- graphs -->
  <script type="text/javascript" src="https://fastly.jsdelivr.net/npm/echarts@5.4.3/dist/echarts.min.js"></script>
  <script type="text/javascript">
    var dom = document.getElementById('graph_a');
    var myChart = echarts.init(dom, null, {
      renderer: 'canvas',
      useDirtyRect: false
    });
    var app = {};
    var option;
    const colors = [
  '#2A8DCE',
  '#D9982D'
];
const dot = [['2021-12', 7833, 2247], ['2022-01', 10440, 2484], ['2022-02', 10554, 2493], ['2022-03', 10843, 2472], ['2022-04', 9928, 2508], ['2022-05', 9401, 2535], ['2022-06', 9325, 2578], ['2022-07', 9623, 2907], ['2022-08', 9260, 2750], ['2022-09', 8914, 2544], ['2022-10', 9200, 2579], ['2022-11', 10706, 2885], ['2022-12', 10102, 2759], ['2023-01', 9773, 2658], ['2023-02', 9494, 2559], ['2023-03', 9224, 2457], ['2023-04', 9005, 2415], ['2023-10', 16315, 1384], ['2023-11', 15707, 1395], ['2023-12', 12969, 1362], ['2024-01', 14356, 1415], ['2024-02', 14229, 1394], ['2024-03', 18645, 1617]];

const dot_x = dot.map(function (item) {
  return item[0];
});
const dot_ipcount = dot.map(function (item) {
  return item[1];
});
const dot_adncount = dot.map(function (item) {
  return item[2];
});

const doh = [['2021-12', 4735, 1005], ['2022-01', 6009, 2884], ['2022-02', 6441, 3130], ['2022-03', 4495, 1245], ['2022-04', 5268, 1279], ['2022-05', 4819, 1322], ['2022-06', 4204, 1355], ['2022-07', 4235, 1566], ['2022-08', 4154, 1496], ['2022-09', 4414, 1519], ['2022-10', 4468, 1551], ['2022-11', 4685, 1502], ['2022-12', 4587, 1413], ['2023-01', 4531, 1366], ['2023-02', 4481, 1316], ['2023-03', 4428, 1279], ['2023-04', 4380, 1252], ['2023-10', 5205, 571], ['2023-11', 4496, 528], ['2023-12', 4364, 544], ['2024-01', 5071, 604], ['2024-02', 4364, 1], ['2024-03', 5071, 564]];

const doh_x = doh.map(function (item) {
  return item[0];
});
const doh_ipcount = doh.map(function (item) {
  return item[1];
});
const doh_adncount = doh.map(function (item) {
  return item[2];
});

const doq = [['2022-07', 1569, 30], ['2022-08', 1722, 51], ['2022-09', 1705, 66], ['2022-10', 1868, 98], ['2022-11', 1910, 101], ['2022-12', 2830, 253], ['2023-03', 3451, 389], ['2023-04', 2294, 395], ['2023-05', 2334, 480], ['2023-10', 3239, 227], ['2023-11', 3321, 273], ['2023-12', 3357, 307], ['2024-01', 3369, 296], ['2024-02', 3357, 223], ['2024-03', 3648, 364]];

const doq_x = doq.map(function (item) {
  return item[0];
});
const doq_ipcount = doq.map(function (item) {
  return item[1];
});
const doq_adncount = doq.map(function (item) {
  return item[2];
});

const doh3 = [['2022-07', 69, 2], ['2022-08', 188, 2], ['2022-09', 140, 2], ['2022-10', 180, 2], ['2022-11', 79, 5], ['2022-12', 74, 4], ['2023-03', 168, 4], ['2023-04', 99, 3], ['2023-05', 95, 3], ['2023-10', 2175, 36], ['2023-11', 2190, 34], ['2023-12', 2384, 33], ['2024-01', 2479, 45], ['2024-02', 2190, 32], ['2024-03', 2190, 31]];

const doh3_x = doh3.map(function (item) {
  return item[0];
});
const doh3_ipcount = doh3.map(function (item) {
  return item[1];
});
const doh3_adncount = doh3.map(function (item) {
  return item[2];
});
var graph_width = '39%';
var graph_hight = '40%';
option = {
  color: colors,
  tooltip: {
    trigger: 'axis',
  },
  toolbox: {
    feature: {
      saveAsImage: { show: true }
    }
  },
  grid: [
    //0 dot
    { height: graph_hight, width: graph_width, left: '5%' },
    //1 doh
    {
      height: graph_hight,
      width: graph_width,
      left: '5%',
      bottom: '3%'
    },
    //2 doq
    { height: graph_hight, width: graph_width, left: '55%' },
    //3 doh3
    { height: graph_hight, width: graph_width, left: '55%', bottom: '3%'}
  ],
  title: [
    { text: 'DOT', left: '23%' },
    { text: 'DOH', left: '23%', bottom: '40%' },
    { text: 'DOQ', left: '73%' },
    { text: 'DOH3', left: '73%', bottom: '40%' }
  ],
  xAxis: [
    {
      show: true, //隐藏了x轴
      type: 'category',
      gridIndex: 0, //对应前面grid的索引位置（第一个）
      axisTick: {
        alignWithLabel: true
      },
      axisLabel: {
        // interval:showNum,  //x轴显示的数量，我这里是动态算的
      },
      data: dot_x
    },
    ////////////
    {
      type: 'category',
      gridIndex: 1, //对应前面grid的索引位置（第二个）
      axisTick: {
        alignWithLabel: true
      },
      axisLabel: {
        //interval:showNum,
      },
      data: doh_x
    },
    ////////////
    {
      type: 'category',
      gridIndex: 2,
      axisTick: {
        alignWithLabel: true
      },
      axisLabel: {
        //interval:showNum,
      },
      data: doq_x
    },
    ////////////
    {
      type: 'category',
      gridIndex: 3,
      axisTick: {
        alignWithLabel: true
      },
      axisLabel: {
        //interval:showNum,
      },
      data: doh3_x
    },
  ],
  yAxis: [
    {
      type: 'value',
      gridIndex: 0,
      name: 'IP Count',
      splitLine: { show: true },
      nameLocation: 'middle',
      nameTextStyle: {
        padding: 30
      },
      position: 'left',
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
      name: 'ADN Count',
      nameTextStyle: {
        padding: 30
      },
      splitLine: { show: false },
      position: 'right',
      axisLine: {
        lineStyle: {
          color: colors[1]
        }
      },
      axisLabel: {
        formatter: '{value}'
      }
    },
    /////////////////
    {
      type: 'value',
      gridIndex: 1,
      name: 'IP Count',
      nameTextStyle: {
        padding: 30
      },
      position: 'left',
      nameLocation: 'middle',
      splitLine: { show: false },
      axisLine: {
        lineStyle: {
          color: colors[0]
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
      name: 'ADN Count',
      nameTextStyle: {
        padding: 30
      },
      nameLocation: 'middle',
      position: 'right',
      splitLine: { show: false },
      axisLine: {
        lineStyle: {
          color: colors[1]
        }
      },
      axisLabel: {
        formatter: '{value}',
        textStyle: {
          fontSize: 12 //y轴坐标轴上的字体大小
        }
      }
    },
    //////////////////
    {
      type: 'value',
      gridIndex: 2,
      name: 'IP Count',
      nameTextStyle: {
        padding: 30
      },
      position: 'left',
      nameLocation: 'middle',
      splitLine: { show: false },
      axisLine: {
        lineStyle: {
          color: colors[0]
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
      gridIndex: 2,
      name: 'ADN Count',
      nameTextStyle: {
        padding: 30
      },
      nameLocation: 'middle',
      position: 'right',
      splitLine: { show: false },
      axisLine: {
        lineStyle: {
          color: colors[1]
        }
      },
      axisLabel: {
        formatter: '{value}',
        textStyle: {
          fontSize: 12 //y轴坐标轴上的字体大小
        }
      }
    },
    //////////////
    {
      type: 'value',
      gridIndex: 3,
      name: 'IP Count',
      nameTextStyle: {
        padding: 30
      },
      position: 'left',
      nameLocation: 'middle',
      splitLine: { show: false },
      axisLine: {
        lineStyle: {
          color: colors[0]
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
      gridIndex: 3,
      name: 'ADN Count',
      nameTextStyle: {
        padding: 30
      },
      nameLocation: 'middle',
      position: 'right',
      splitLine: { show: false },
      axisLine: {
        lineStyle: {
          color: colors[1]
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
      name: 'DOT IP Count',
      type: 'bar',
      xAxisIndex: 0,
      yAxisIndex: 0,
      data: dot_ipcount,
      color: colors[0],
      barMaxWidth: 20
    },
    {
      name: 'DOT ADN Count',
      type: 'line',
      xAxisIndex: 0,
      yAxisIndex: 1,
      data: dot_adncount,
      color: colors[1]
    },
    ////////////////
    {
      name: 'DOH IP Count',
      type: 'bar',
      xAxisIndex: 1,
      yAxisIndex: 2,
      data: doh_ipcount,
      color: colors[0],
      barMaxWidth: 20
    },
    {
      name: 'DOH ADN Count',
      type: 'line',
      xAxisIndex: 1,
      yAxisIndex: 3,
      data: doh_adncount,
      color: colors[1]
    },
    ////////////////
    {
      name: 'DOQ IP Count',
      type: 'bar',
      xAxisIndex: 2,
      yAxisIndex: 4,
      data: doq_ipcount,
      color: colors[0],
      barMaxWidth: 20
    },
    {
      name: 'DOQ ADN Count',
      type: 'line',
      xAxisIndex: 2,
      yAxisIndex: 5,
      data: doq_adncount,
      color: colors[1]
    },
    ////////////////
    {
      name: 'DOH3 IP Count',
      type: 'bar',
      xAxisIndex: 3,
      yAxisIndex: 6,
      data: doh3_ipcount,
      color: colors[0],
      barMaxWidth: 20
    },
    {
      name: 'DOH3 ADN Count',
      type: 'line',
      xAxisIndex: 3,
      yAxisIndex: 7,
      data: doh3_adncount,
      color: colors[1]
    },
  ]
};
    if (option && typeof option === 'object') {
      myChart.setOption(option);
    }

    window.addEventListener('resize', myChart.resize);
  </script>

<!-- graph b -->
<script type="text/javascript">
    var dom = document.getElementById('graph_b');
    var myChart = echarts.init(dom, null, {
      renderer: 'canvas',
      useDirtyRect: false
    });
    var app = {};
    
    var option;

const valid = [['2021-12', 0.7760755776841568, 0.9324181626187962, 0, 0], ['2022-01', 0.6272988505747127, 0.7109335996005991, 0, 0], ['2022-02', 0.6227022929694902, 0.7404129793510325, 0, 0], ['2022-03', 0.6085031817762612, 0.9276974416017798, 0, 0], ['2022-04', 0.6645850120870266, 0.936408504176158, 0, 0], ['2022-05', 0.6997127965110095, 0.9223905374559037, 0, 0], ['2022-06', 0.6913672922252011, 0.9112749762131304, 0, 0], ['2022-07', 0.6895978385118986, 0.9010625737898466, 0.9974506054811982, 1.0], ['2022-08', 0.7014038876889849, 0.8991333654309099, 0.9936120789779327, 1.0], ['2022-09', 0.7293022212250393, 0.8994109651110104, 0.9847507331378299, 1.0], ['2022-10', 0.7204347826086956, 0.9015219337511191, 0.9753747323340471, 1.0], ['2022-11', 0.6301139547917056, 0.9054429028815368, 0.9664921465968587, 1.0], ['2022-12', 0.649574341714512, 0.8968824940047961, 0.9614840989399294, 1.0], ['2023-01', 0.6582420955694259, 0.8874420657691459, 0, 0], ['2023-02', 0.6687381504107858, 0.8917652309752288, 0, 0], ['2023-03', 0.6835429314830876, 0.8873080397470642, 0.944943494639235, 1.0], ['2023-04', 0.6957245974458635, 0.8872146118721461, 0.9350479511769835, 1.0], ['2023-10', 0.6250076616610482, 0.8975984630163305, 0.9617165791911083, 0.9972413793103448], ['2023-11', 0.6625708282931178, 0.9332740213523132, 0.959349593495935, 0.997716894977169], ['2023-12', 0.6201711774230858, 0.9319431714023831, 0.9579982126899017, 0.99748322147651], ['2024-01', 0.7038172192811368, 0.8964701242358509, 0.9531018106262986, 0.9971762807583703], ['2024-02', 0.7144563918757467, 0.9319431714023831, 0.9579982126899017, 0.997716894977169], ['2024-03', 0.5556985787074282, 0.8964701242358509, 0.9385964912280702, 0.997716894977169]];

const valid_x = valid.map(function (item) {
  return item[0];
});
const valid_dot = valid.map(function (item) {
  return item[1];
});
const valid_doh = valid.map(function (item) {
  return item[2];
});
const valid_doq = valid.map(function (item) {
  return item[3];
});
const valid_doh3 = valid.map(function (item) {
  return item[4];
});

const self_signed = [['2021-12', 0.16992212434571685, 0.013093980992608237, 0, 0], ['2022-01', 0.3282567049808429, 0.0068230986853053755, 0, 0], ['2022-02', 0.3349440970248247, 0.007297003570874088, 0, 0], ['2022-03', 0.34971871253343173, 0.012458286985539488, 0, 0], ['2022-04', 0.28807413376309426, 0.012148823082763858, 0, 0], ['2022-05', 0.2514626103605999, 0.015148371031334302, 0, 0], ['2022-06', 0.2551206434316354, 0.017602283539486202, 0, 0], ['2022-07', 0.25033773251584746, 0.018417945690672965, 0.0025493945188017845, 0.0], ['2022-08', 0.23855291576673865, 0.01853635050553683, 0.005807200929152149, 0.0], ['2022-09', 0.212474758806372, 0.02084277299501586, 0.00997067448680352, 0.0], ['2022-10', 0.22554347826086957, 0.020590868397493287, 0.011777301927194861, 0.0], ['2022-11', 0.3182327666728937, 0.017502668089647812, 0.015183246073298429, 0.0], ['2022-12', 0.2939021975846367, 0.01591454109439721, 0.01696113074204947, 0.0], ['2023-01', 0.2814898188887752, 0.017214742882365925, 0, 0], ['2023-02', 0.2676427217189804, 0.012720374916313323, 0, 0], ['2023-03', 0.25314397224631396, 0.012195121951219513, 0.01883512025499855, 0.0], ['2023-04', 0.23986674069961134, 0.012100456621004566, 0.023103748910200523, 0.0], ['2023-10', 0.31467974256818876, 0.02862632084534102, 0.009262117937635072, 0.001379310344827586], ['2023-11', 0.2806392054497995, 0.023354092526690393, 0.011141222523336344, 0.0013698630136986301], ['2023-12', 0.31567584239339963, 0.02383134738771769, 0.011319630622579685, 0.0012583892617449664], ['2024-01', 0.23216773474505434, 0.03036876355748373, 0.011872959335114277, 0.0004033884630899556], ['2024-02', 0.22334668634478883, 0.02383134738771769, 0.011319630622579685, 0.0013698630136986301], ['2024-03', 0.39152587825154195, 0.03036876355748373, 0.018914473684210526, 0.0013698630136986301]];

const self_signed_x = self_signed.map(function (item) {
  return item[0];
});
const self_signed_dot = self_signed.map(function (item) {
  return item[1];
});
const self_signed_doh = self_signed.map(function (item) {
  return item[2];
});
const self_signed_doq = self_signed.map(function (item) {
  return item[3];
});
const self_signed_doh3 = self_signed.map(function (item) {
  return item[4];
});

option = {
  title: [
    {
      text: 'Valid',
      left: '25%'
    },
    {
      text: 'Self-signed',
      left: '73%'
    }
  ],
  tooltip: {
    trigger: 'axis'
  },
  legend: [
    {
      data: ['DOT', 'DOH', 'DOQ', 'DOH3'],
      left: '41%',
      top: '2.5%'
    }
  ],
  grid: [
    {
      left: '3%',
      bottom: '3%',
      width: '45%',
      containLabel: true
    },
    {
      left: '50%',
      bottom: '3%',
      width: '45%',
      containLabel: true
    }
  ],
  toolbox: {
    feature: {
      saveAsImage: { show: true }
    }
  },
  xAxis: [
    {
      gridIndex: 0,
      type: 'category',
      boundaryGap: false,
      data: valid_x
    },
    {
      gridIndex: 1,
      type: 'category',
      boundaryGap: false,
      data: self_signed_x,
    }
  ],
  yAxis: [
    {
      gridIndex: 0,
      type: 'value'
    },
    {
      gridIndex: 1,
      type: 'value'
    }
  ],
  series: [
    {
      name: 'DOT',
      type: 'line',
      stack: 'Total',
      xAxisIndex: 0,
      yAxisIndex: 0,
      data: valid_dot
    },
    {
      name: 'DOH',
      type: 'line',
      // stack: 'Total',
      xAxisIndex: 0,
      yAxisIndex: 0,
      data: valid_doh
    },
    {
      name: 'DOQ',
      type: 'line',
      // stack: 'Total',
      xAxisIndex: 0,
      yAxisIndex: 0,
      data: valid_doq
    },
    {
      name: 'DOH3',
      type: 'line',
      // stack: 'Total',
      xAxisIndex: 0,
      yAxisIndex: 0,
      data: valid_doh3
    },
    ////////////////////
    {
      name: 'DOT',
      type: 'line',
      // stack: 'Total',
      xAxisIndex: 1,
      yAxisIndex: 1,
      data: self_signed_dot
    },
    {
      name: 'DOH',
      type: 'line',
      // stack: 'Total',
      xAxisIndex: 1,
      yAxisIndex: 1,
      data: self_signed_doh
    },
    {
      name: 'DOQ',
      type: 'line',
      // stack: 'Total',
      xAxisIndex: 1,
      yAxisIndex: 1,
      data: self_signed_doq
    },
    {
      name: 'DOH3',
      type: 'line',
      // stack: 'Total',
      xAxisIndex: 1,
      yAxisIndex: 1,
      data: self_signed_doh3
    },
  ]
};


    if (option && typeof option === 'object') {
      myChart.setOption(option);
    }

    window.addEventListener('resize', myChart.resize);
  </script>

<br>

## Raw data

We provide open access to raw data from the two most recent scans.
Drop us an [email](mailto:luchaoyi@tsinghua.edu.cn) if you need scanning results from other months.

| Description         | DoT servers                                | DoH servers                                | DoQ servers                                | DoH3 servers                                 |
| ------------ | ------------------------------------------ | ------------------------------------------ | ------------------------------------------ | -------------------------------------------- |
| March 2024 (IPv4) | [dot-202403.json](/files/dot-2024-03.json) | [doh-202403.json](/files/doh-2024-03.json) | [doq-202403.json](/files/doq-2024-03.json) | [doh3-202403.json](/files/doh3-2024-03.json) |
| February 2024 (IPv4) | [dot-202402.json](/files/dot-2024-02.json) | [doh-202402.json](/files/doh-2024-02.json) | [doq-202402.json](/files/doq-2024-02.json) | [doh3-202402.json](/files/doh3-2024-02.json) |
| DoE domains (with IPv6) | [dot-domain-v6.txt](/files/dot-domain-v6.txt) | [doh-domain-v6.txt](/files/doh-domain-v6.txt) | [doq-domain-v6.txt](/files/doq-domain-v6.txt) | [doh3-domain-v6.txt](/files/doh3-domain-v6.txt) |
