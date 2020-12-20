<script>
import { Doughnut } from 'vue-chartjs'

export default {
  extends: Doughnut,
  props: ['chartdata', 'options'],
// {
//     chartdata: {
//       type: Object,
//       default: ['ETF', 'Stock', 'Bonds']
//     },
//     options: {
//       type: Object,
//       default: null
//     }
//   },
  mounted() {
    this.renderChart(this.chartdata, {responsive: true});
    // {
    // labels: ['ETF', 'Stock', 'Bds'],
    // datasets: [
    //   {
    //     label: 'GitHub Commits',
    //     backgroundColor: ['#086004','#660732', '#8f8b11'],
    //     data: [70, 20, 10]
    //   }
    // ]
    // }
  // )
}
,
}
</script>
<style>
@keyframes appear {
  0% {
    opacity: 0;
  }
}
</style>
