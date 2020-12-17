<template>
  <div>
    <div class="row">
      <div>
        <b-form-datepicker
          id="example-datepicker"
          v-model="form.date"
          class="mb-2"
        ></b-form-datepicker>
      </div>
      <div>
        <b-form-input v-model="form.ticker" placeholder="Ticker"></b-form-input>
      </div>
      <div>
        <b-form-input v-model="form.shares" placeholder="# of Shares"></b-form-input>
      </div>
      <div>
        <b-form-select
          v-model="form.account_id"
          :options="accounts"
        ></b-form-select>
      </div>
      <div>
        <b-form-input v-model="form.price_per_share" placeholder="Cost Basis"></b-form-input>
      </div>
      <div>
        <b-form-select
          v-model="form.type_id"
          :options="investmentTypes"
        ></b-form-select>
      </div>
      <div>
        <b-button variant="primary" @click="addInvestment">Add</b-button>
      </div>
    </div>
    <div class="row">
      <div class="col-4">
<!--        <b-table-->
<!--          hover-->
<!--          :items="summary"-->
<!--          :fields="categories"-->
<!--          striped-->
<!--          responsive="sm"-->
<!--        ></b-table>-->
        <h5>Investment Types</h5>
        <b-list-group>
          <b-list-group-item v-for="invest_type in investmentTypes">
            <b-row>
              <b-col>
                {{ invest_type.text }}
              </b-col>
            </b-row>
          </b-list-group-item>
          <b-list-group-item>
            <b-form inline>
              <b-form-input
                id="input-1"
                type="text"
                v-model="new_investment_type"
                placeholder="Enter new category"
                required
              ></b-form-input>
              <b-button @click="addInvestmentType">Add</b-button>
            </b-form>
          </b-list-group-item>
        </b-list-group>
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
import Vue from 'vue'
import DoughnutChart from '~/components/DoughnutChart'
import StackedAreaChart from '~/components/StackedAreaChart'
import StackedLineChart from '~/components/StackedLineChart'

export default Vue.extend({
  components: { StackedLineChart, StackedAreaChart, DoughnutChart },
  data() {
    return {
      // selectedcategories: 'ETF',
      categories: ['etf', 'stock', 'crypto', 'bonds'],
      // selectedaccount: 'TDA',
      accounts: [],
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
        'cost_basis',
        'shares',
        'value_change',
        'prev_year_dividend	',
        'estDividend',
        'actual_allocation',
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
      ],
      form: {
        account_id: null,
        ticker: '',
        shares: '',
        type_id: null,
        price_per_share: null,
        date: null
      },
      investmentTypes: [],
      new_investment_type: ''
    }
  },
  mounted() {
    this.getAccounts()
    this.getInvestmentTypes()
    this.getInvestments()
  },
  methods: {
    async getAccounts() {
      let res = await this.$axios.$get('/accounts')
      const accounts = []
      res.accounts.assets.forEach(acc => {
        accounts.push({ value: acc.id, text: acc.name[0].toUpperCase() + acc.name.substr(1).toLowerCase() })
      })
      this.form.account_id = accounts[0].value
      this.accounts = accounts
    },
    async getInvestmentTypes() {
      let res = await this.$axios.$get('/investment/type')
      const investmentTypes = []
      res.investment_types.forEach(type => {
        investmentTypes.push({ value: type.id, text: type.name})
      })
      this.form.type_id = investmentTypes[0].value
      this.investmentTypes = investmentTypes
    },
    async getInvestments() {
      let res = await this.$axios.$get('/investment')
      this.items=res.investments
    },
    async addInvestmentType() {
      await this.$axios.post('/investment/type', { name: this.new_investment_type })
      this.new_investment_type = ''
      this.getInvestmentTypes()
    },
    async addInvestment() {
      const myDate = this.$moment(new Date(this.form.date)).format('YYYY-MM-DD HH:mm:ss')
      const investment = {
        'investment_type_id': this.form.type_id,
        'ticker': this.form.ticker,
        'shares': this.form.shares,
        'price_per_share': this.form.price_per_share,
        'date': myDate,
        'investment_account_id': this.form.account_id
      }
      console.log(investment)
      await this.$axios.post('/investment', investment)
      this.getInvestments()
    }
  }
})
</script>
<style>
@keyframes appear {
  0% {
    opacity: 0;
  }
}
</style>
