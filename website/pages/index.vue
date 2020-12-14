<template>
  <div>
    <Expense />
    <div class="row">
      <div class="col-4">
        <b-table
          hover
          thead-class="no_header"
          :items="goals"
          :fields="fields"
          striped
          responsive="sm"
        >
          <template #cell(percent)="row">
            <b-progress :max="max" height="2rem">
              <b-progress-bar :value="row.item.percent">
                <span><strong>{{ row.item.percent }} / {{ row.item.max }}</strong></span>
              </b-progress-bar>
            </b-progress>
            <!-- As `row.showDetails` is one-way, we call the toggleDetails function on @change -->
          </template>
        </b-table>
      </div>
      <div class="col-4">
        <b-table
          hover
          thead-class="no_header"
          :items="systemoptions"
          striped
          responsive="sm"
        ></b-table>
      </div>
      <div class="col-4">
        <div>
          Expenses Covered
          <DoughnutChart />
        </div>
        <div>
          Expenses Covered
          <DoughnutChart />
        </div>
        <div>
        </div>
      </div>

    </div>
    <div class="row">
      <div class="col-6">
        Net Worth
        <StackedAreaChart />
      </div>
      <div class="col-6">
        Cash Flow
        <StackedAreaChart />
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import Vue from 'vue'
import DoughnutChart from '~/components/DoughnutChart.vue'
import StackedAreaChart from '~/components/StackedAreaChart.vue'

export default Vue.extend({
  components: { StackedAreaChart, DoughnutChart },
  data() {
    return {
      fields: ['label', 'percent'],
      goals: [
        { label: 'Growth', percent: 10, max: '' },
        { label: '100K', percent: 20000, max: 100000 },
        { label: '200K', percent: 0.1 },
        { label: '500K', percent: 0.001 },
        { label: '1M', percent: 0 },
        { label: '2M', percent: 0 },
        { label: '5M', percent: 0 },
        { label: '10M', percent: 0 },
        { label: 'Percent to FI', percent: -12 },
        { label: 'Year of Expenses', percent: '12 Years' },
        { label: 'Years to FI', percent: '4 Years' },
        { label: 'Current Safe Withdrawal Rate', percent: '$4000' }
      ],
      systemoptions: [
        ['Include Equity', 'FALSE'],
        ['Use Budget?', 'FALSE'],
        ['Withdrawal Rate', '3.75%'],
        ['Return Rate', '7%'],
        ['Expense Year', '2021'],
        ['Avg. Local Tax', '20%'],
        ['Desired Retire Date', 'May 2050'],
        ['Yearly Requirement', '9350925'],
        ['Annual Savings', '50925'],
        ['Est. Yearly Expense', '9999'],
        ['FI Number', '395029350'],
        ['Total Net Worth', '59305'],
        ['Total Net Worth Hourly Increase', '59'],
        ['Total Net Worth Hourly Wage', '59']
      ]

    }
  }
})
</script>

<style>
.container {
  margin: 0 auto;
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
}

.no_header {
  display: none;
}

.title {
  font-family: 'Quicksand', 'Source Sans Pro', -apple-system, BlinkMacSystemFont,
  'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
  display: block;
  font-weight: 300;
  font-size: 100px;
  color: #35495e;
  letter-spacing: 1px;
}

.subtitle {
  font-weight: 300;
  font-size: 42px;
  color: #526488;
  word-spacing: 5px;
  padding-bottom: 15px;
}

.links {
  padding-top: 15px;
}
</style>
