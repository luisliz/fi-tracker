<template>
  <div>
    <div class="row">
      <div>
        <b-form-datepicker id="example-datepicker" v-model="form.date" class="mb-2"></b-form-datepicker>
      </div>
      <div>
        <b-form-select v-model="form.budget_id" :options="budget_categories"></b-form-select>
      </div>
      <div>
        <b-form-select v-model="form.account_id" :options="accounts"></b-form-select>
      </div>
      <div>
        <b-form-input v-model="form.paid_to" placeholder="Paid To"></b-form-input>
      </div>
      <div>
        <b-form-input v-model="form.amount" placeholder="Amount"></b-form-input>
      </div>
      <div>
        <b-button variant="primary" @click="addExpense">Add</b-button>
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
            <b-col sm="3" class="text-sm-right"><b>Budget:</b></b-col>
            <b-col>{{ row.item.budget }}</b-col>
          </b-row>

          <b-row class="mb-2">
            <b-col sm="3" class="text-sm-right"><b>Year Average:</b></b-col>
            <b-col>{{ row.item.year_average }}</b-col>
          </b-row>
          <b-row class="mb-2">
            <b-col sm="3" class="text-sm-right"><b>Annual:</b></b-col>
            <b-col>{{ row.item.annual }}</b-col>
          </b-row>
          <b-row class="mb-2">
            <b-col sm="3" class="text-sm-right"><b>Savings:</b></b-col>
            <b-col>{{ row.item.savings }}</b-col>
          </b-row>
        </b-card>
      </template>
    </b-table>

  </div>
</template>

<script>
import Vue from 'vue'

export default Vue.extend({
  data() {
    return {
      form: {
        date: null,
        budget_id: null,
        account_id: null,
        paid_to: '',
        amount: null
      },
      budget_categories: [],
      expenses: [],
      accounts: [],
      fields: ['expense_date', 'budget_name', 'paid_to', 'from_account', 'amount', 'show_details'],
      items: []
    }
  },
  mounted() {
    this.getAccounts()
    this.getBudgetCategories()
    this.getExpenses()
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
    async getBudgetCategories() {
      const categories = await this.$axios.$get('/budget/category')

      let new_categories = []
      categories.budget_categories.forEach((cat) => {
        new_categories.push({ text: cat.name, value: cat.id })
      })
      this.budget_categories = new_categories
      this.form.budget_id = new_categories[0].value
    },
    async getExpenses() {
      const res = await this.$axios.$get('/budget/expense')
      this.items = res.expenses
    },
    async addExpense() {
      const myDate = this.$moment(new Date(this.form.date)).format('YYYY-MM-DD HH:mm:ss')
      const expense = {
        'amount': this.form.amount,
        'expense_date': myDate,
        'paid_to': this.form.paid_to,
        'budget_entry_id': this.form.budget_id,
        'account_id': this.form.account_id
      }
      await this.$axios.post('/budget/expense', expense)
      this.getExpenses()
    }
  }

})
</script>
