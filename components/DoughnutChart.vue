<script>
import { Doughnut } from 'vue-chartjs'

export default {
  extends: Doughnut,
  props: {
    chartdata: {
      type: Object,
      default: null
    },
    options: {
      type: Object,
      default: null
    }
  },
  mounted() {
    this.renderChart({
      labels: ['ETF', 'Stock', 'Bonds'],
      datasets: [
        {
          label: 'GitHub Commits',
          backgroundColor: ['#086004','#660732', '#8f8b11'],
          data: [70, 20, 10]
        }
      ]
    })
  },
}
</script>
<style>
@keyframes appear {
  0% {
    opacity: 0;
  }
}
</style>
