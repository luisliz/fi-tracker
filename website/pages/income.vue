<template>
  <div class="row m-3">
    <div class="col-9">
      <div class="row">
        <div>
          <b-form-datepicker v-model="form.date" id="example-datepicker" class="mb-2"></b-form-datepicker>
        </div>
        <div>
          <b-form-select v-model="form.income_id" :options="incomes"></b-form-select>
        </div>
        <div>
          <b-form-input v-model="form.source" placeholder="Source"></b-form-input>
        </div>
        <div>
          <b-form-input v-model="form.amount" placeholder="Amount"></b-form-input>
        </div>
        <div>
          <b-form-select v-model="form.account" :options="accounts"></b-form-select>
        </div>
        <div>
          <b-button variant="primary" @click="addIncome">Add</b-button>
        </div>
      </div>

      <b-table hover :items="items" :fields="fields" striped responsive="sm">
        <template #cell(show_details)="row">
          <b-button size="sm" @click="row.toggleDetails" class="mr-2">
            {{ row.detailsShowing ? 'Hide' : 'Show' }} Details
          </b-button>

          <!-- As `row.showDetails` is one-way, we call the toggleDetails function on @change -->
        </template>

        <template #row-details="row">
          <b-card>
            <b-row class="mb-2">
              <b-col sm="3" class="text-sm-right"><b>Taxes:</b></b-col>
              <b-col>{{ row.item.taxes }}</b-col>
            </b-row>

            <b-row class="mb-2">
              <b-col sm="3" class="text-sm-right"><b>Saved:</b></b-col>
              <b-col>{{ row.item.savings }}</b-col>
            </b-row>
            <b-row class="mb-2">
              <b-col sm="3" class="text-sm-right"><b>401k:</b></b-col>
              <b-col>{{ row.item.k401 }}</b-col>
            </b-row>
            <b-row class="mb-2">
              <b-col sm="3" class="text-sm-right"><b>ROTH IRA:</b></b-col>
              <b-col>{{ row.item.roth }}</b-col>
            </b-row>
            <div class="dropdown-divider"></div>
            <b-row class="mb-2">
              <b-col sm="3" class="text-sm-right"><b>Net Income:</b></b-col>
              <b-col>{{ row.item.net }}</b-col>
            </b-row>
          </b-card>
        </template>
      </b-table>
    </div>
    <div class="col-3">
      <h5>Income Types</h5>
      <b-list-group>
        <b-list-group-item v-for="income in incomes">
          <b-row>
            <b-col>
              {{ income.text }}
            </b-col>
          </b-row>
        </b-list-group-item>
        <b-list-group-item>
          <b-form inline>
            <b-form-input
              id="input-1"
              type="text"
              v-model="newIncomeType"
              placeholder="Enter new category"
              required
            ></b-form-input>
            <b-button @click="addIncomeType">Add</b-button>
          </b-form>
        </b-list-group-item>
      </b-list-group>
    </div>
  </div>
</template>

<script>
import Vue from 'vue'

export default Vue.extend({
  data() {
    return {
      // selectedincome: 'job',
      // selectedincometype: 'payment',
      incomes: [],
      // selectedaccount: 'Cash',
      accounts: [],
      // incometype: [],
      fields: ['source', 'account_name', 'type', 'amount', 'date', 'show_details'],
      items: [],
      newIncomeType: '',
      form: {
        income_id: null,
        account: null,
        amount: null,
        source: ''
      }
    }
  },
  mounted() {
    this.getIncomeTypes()
    this.getAccounts()
    this.getIncomes()
  },
  methods: {
    async getIncomeTypes() {
      let incomes = await this.$axios.$get('/income/type')

      let new_incomes = []
      incomes.income_types.forEach((income) => {
        new_incomes.push({ text: income.name, value: income.id })
      })

      this.form.income_id = new_incomes[0].value
      this.incomes = new_incomes
    },
    async addIncomeType() {
      await this.$axios.post('/income/type', { name: this.newIncomeType })
      this.getIncomeTypes()

    },
    async getIncomes() {
      const res = await this.$axios.$get('/income')
      this.items = res.incomes
    },
    async addIncome() {
      const income = {
        'source': this.form.source,
        'amount': this.form.amount,
        'income_date': '2020-12-16T18:02:07.208Z',
        'taxes': 0,
        'saved': 0,
        'income_type_id': this.form.income_id,
        'account_id': this.form.account
      }
      const res = await this.$axios.post('/income', income)
     console.log(res)
      this.getIncomes()
    },
    async getAccounts() {
      let res = await this.$axios.$get('/accounts')
      const accounts = []
      res.accounts.assets.forEach(acc => {
        accounts.push({ value: acc.id, text: acc.name[0].toUpperCase() + acc.name.substr(1).toLowerCase() })
      })
      this.form.account = accounts[0].value
      this.accounts = accounts
    }

  }

})
</script>
