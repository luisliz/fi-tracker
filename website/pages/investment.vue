<template>
  <div>
    <div class="row">
      <div>
        <b-form-datepicker
          id="example-datepicker"
          v-model="value"
          class="mb-2"
        ></b-form-datepicker>
      </div>
      <div>
        <b-form-input placeholder="Ticker"></b-form-input>
      </div>
      <div>
        <b-form-input placeholder="# of Shares"></b-form-input>
      </div>
      <div>
        <b-form-select
          v-model="selectedaccount"
          :options="accounts"
        ></b-form-select>
      </div>
      <div>
        <b-form-input placeholder="Cost Basis"></b-form-input>
      </div>
      <div>
        <b-form-select
          v-model="selectedcategories"
          :options="categories"
        ></b-form-select>
      </div>
      <div>
        <b-button variant="primary">Add</b-button>
      </div>
    </div>
    <div class="row">
      <div class="col-4">
        <b-table
          hover
          :items="summary"
          :fields="categories"
          striped
          responsive="sm"
        ></b-table>
      </div>
      <div class="col-4">
        <DoughnutChart />
      </div>
      <div class="col-4">
        <DoughnutChart />
      </div>
    </div>
    <b-table
      hover
      :items="items"
      :fields="fields"
      striped
      responsive="sm"
    ></b-table>
    <div class="row">
      <div class="col-4">
        Cost vs P&L
        <StackedAreaChart />
      </div>
      <div class="col-4">
        ETF P&L
        <StackedAreaChart />
      </div>
      <div class="col-4">
        Stock P&L
        <StackedAreaChart />
      </div>
    </div>
    <div>
      <StackedLineChart />
    </div>
    <b-table
      hover
      :items="fulltableitems"
      :fields="fulltablefields"
      striped
      responsive="sm"
    ></b-table>
  </div>
</template>

<script>
import DoughnutChart from '~/components/DoughnutChart'
import StackedAreaChart from '~/components/StackedAreaChart'
import StackedLineChart from '~/components/StackedLineChart'

export default {
  components: { StackedLineChart, StackedAreaChart, DoughnutChart },
  data() {
    return {
      selectedcategories: 'ETF',
      categories: ['etf', 'stock', 'crypto', 'bonds'],
      selectedaccount: 'TDA',
      accounts: ['TDA', 'Vanguard'],
      summary: [
        { etf: '40%', stock: '50%', crypto: '0%', bonds: '10%' },
        {
          etf: '$85,1082.00',
          stock: '$85,050.00',
          crypto: '$20.00',
          bonds: '$100,843.00'
        }
      ],
      fields: [
        'category',
        'ticker',
        'valuePerShare',
        'shares',
        'value_change',
        'prev_year_dividend	',
        'estDividend',
        'actual_allocation',
        'target_allocation'
      ],
      items: [
        {
          category: 'ETF',
          ticker: 'VTI',
          valuePerShare: '$190.18',
          shares: '2',
          value_change: '+3%',
          prev_year_dividend: '$0.74',
          estDividend: '$10',
          actual_allocation: '20%',
          target_allocation: '50%'
        }
      ],
      fulltablefields: [
        'etf1',
        'etf2',
        'stock1',
        'stock2',
        'total_cost_basis',
        'cost_basis',
        'totalPortfolioValue',
        'profit/loss',
        'monthProfit/Loss',
        'totalSpent',
        'etf_p/l',
        'stock_p/l'
      ],
      fulltableitems: [
        {
          etf1: '$20',
          etf2: '$500',
          stock1: '$0',
          stock2: '$9590',
          total_cost_basis: '$10900',
          cost_basisDiff: '+500',
          totalPortfolioValue: '$501040',
          profit_loss: '-50',
          totalSpent: '$500',
          etf_l_l: '+500',
          stock_p_l: '-5000'
        }
      ]

    }
  }
}
</script>
<style>
@keyframes appear {
  0% {
    opacity: 0;
  }
}
</style>
