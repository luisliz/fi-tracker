<template>
  <div>
    <div class="m-3">
      <h3>✨Investments✨</h3>

      <b-row>
        <b-col v-if="loadChart">
          <DoughnutChart :chartdata="chartdata" />
        </b-col>

        <!--        <b-col>
                  Cost vs P&L
                  <StackedAreaChart />
        <b-col>-->


        <!--   <div class="row">
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
           ></b-table>-->

        <b-col>
          <h5>Investment Types</h5>
          <b-row>
            <b-col>
              <b-form-group label="Date:">
                <b-form-datepicker v-model="form.date"></b-form-datepicker>
              </b-form-group>
            </b-col>
            <b-col>
              <b-form-group label="Ticker:">
                <b-form-input v-model="form.ticker" placeholder="Ticker"></b-form-input>
              </b-form-group>
            </b-col>
          </b-row>
          <b-row>
            <b-col>
              <b-form-group label="Shares:">
                <b-form-input v-model="form.shares" placeholder="# of Shares"></b-form-input>
              </b-form-group>
            </b-col>
            <b-col>
              <b-form-group label="Price:">
                <b-form-input v-model="form.price_per_share" placeholder="Price per share"></b-form-input>
              </b-form-group>
            </b-col>
          </b-row>
          <b-row>
            <b-col>
              <b-form-group label="Account:">
                <b-form-select v-model="form.account_id" :options="accounts"
                ></b-form-select>
              </b-form-group>
            </b-col>
            <b-col>
              <b-form-group label="Investment Type:">
                <b-form-select v-model="form.type_id" :options="investmentTypes"
                ></b-form-select>
              </b-form-group>
            </b-col>
          </b-row>
          <b-button variant="outline-success" block @click="addInvestment">Add</b-button>
        </b-col>
        <b-col>
          <!--       <b-table
                   hover
                   :items="summary"
                   :fields="categories"
                   striped
                   responsive="sm"
                 ></b-table>-->
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
        </b-col>
      </b-row>
      <b-table
        hover
        :items="items"
        :fields="fields"
        striped
        responsive="sm"
      ></b-table>

    </div>

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
      fmt: new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD' }),
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
      loadChart: false,
      fields: [
        'investment_type',
        'ticker',
        'shares',
        // 'value_per_share',
        {
          key: 'value_per_share',
          formatter: value => value ? this.fmt.format(value) : '-'
        },
        {
          key: 'value_change',
          formatter: value => {
            return value ? value.toFixed(2) + '%' : '-'
          }
        },
        {
          key: 'cost_basis',
          formatter: value => value ? this.fmt.format(value) : '-'
        },
        {
          key: 'est_total_quarter_dividend',
          formatter: value => value ? this.fmt.format(value) : '-'
        },
        {
          key: 'total_value',
          formatter: value => value ? this.fmt.format(value) : '-'
        },
        {
          key: 'actual_allocation',
          formatter: value => {
            return value ? value + '%' : '-'
          }
        }
      ],
      chartdata: {},
      items: [],
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
        investmentTypes.push({ value: type.id, text: type.name })
      })
      this.form.type_id = investmentTypes[0].value
      this.investmentTypes = investmentTypes
    },
    async getInvestments() {
      let res = await this.$axios.$get('/investment')

      this.items = res.investments

      let doughnut = {
        labels: [],
        datasets: [
          {
            label: 'GitHub Commits',
            backgroundColor: [
              'rgba(255, 99, 132, 1)',
              'rgba(54, 162, 235, 1)',
              'rgba(255, 206, 86, 1)',
              'rgba(139,217,129, 1)',
              'rgba(153, 102, 255, 1)',
              'rgba(200,251,197, 1)',
              'rgba(66, 179, 129, 1)',
              'rgba(75, 192, 192, 1)',
              'rgba(255, 138, 64, 1)',
              'rgba(86, 85, 14, 1)',
              'rgba(38,84,187, 1)',
              'rgba(255, 138, 64, 1)',
              'rgba(255, 138, 64, 1)',
              'rgba(255, 138, 64, 1)'
            ],
            data: []
          }
        ]
      }
      // const doughnutjson = JSON.parse(res.doughnut)
      // console.log(doughnutjson.length())
      res.doughnut.forEach(part => {
        doughnut.labels.push(part[0])
        doughnut.datasets[0].data.push(part[1])
      })
      this.chartdata = doughnut
      this.loadChart = true


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

      this.loadChart = false
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
