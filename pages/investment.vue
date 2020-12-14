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
        <DoughnutChart/>
      </div>
      <div class="col-4">
        <DoughnutChart/>
      </div>
    </div>
    <b-table
      hover
      :items="items"
      :fields="fields"
      striped
      responsive="sm"
    ></b-table>
  </div>
</template>

<script>
import DoughnutChart from "~/components/DoughnutChart";
export default {
  components: {DoughnutChart},
  data() {
    return {
      selectedcategories: 'ETF',
      categories: ['etf', 'stock', 'crypto', 'bonds'],
      selectedaccount: 'TDA',
      accounts: ['TDA', 'Vanguard'],
      summary: [
        {etf: '40%', stock: '50%', crypto: '0%', bonds: '10%'},
        {
          etf: '$85,1082.00',
          stock: '$85,050.00',
          crypto: '$20.00',
          bonds: '$100,843.00',
        },
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
        'target_allocation',
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
          target_allocation: '50%',
        },
      ],
    }
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
