<template>
  <div class="m-3 row">

    <div class="col-9">
      <h3 class="row">
        Budget
      </h3>
      <b-table hover :items="budget_entries" :fields="fields" striped responsive="sm"></b-table>
    </div>
    <div class="border-left col-3">
      <b-col>
        <h5> Add New Budget Entry</h5>
        <b-form-group
          label="Entry Name:"
          label-for="budget-name"
        >
          <b-form-input id="budget-name" v-model="form.name" placeholder="Name"></b-form-input>
        </b-form-group>
        <b-form-group
          label="Category:"
          label-for="budget-category"
        >
          <b-form-select id="budget-category" v-model="form.category_id" :options="budget_categories"></b-form-select>
        </b-form-group>
        <b-form-group
          label="Importance:"
          label-for="budget-importance"
        >
          <b-form-select id="budget-importance" v-model="form.importance" :options="importance"></b-form-select>
        </b-form-group>
        <b-form-group
          label="Amount Budgeted:"
          label-for="budget-amount"
        >
          <b-form-input id="budget-amount" v-model="form.amount" placeholder="Amount"></b-form-input>
        </b-form-group>

        <b-button id="budget-name" variant="outline-success" block @click="addBudgetEntry">Add</b-button>

      </b-col>
      <b-col class="pt-2 border-top">
        <h5> Current Categories</h5>
        <b-list-group>
          <b-list-group-item v-for="category in budget_categories">
            <b-row>
              <b-col>
                {{ category.text }}
              </b-col>
            </b-row>
          </b-list-group-item>
          <b-list-group-item>
            <b-form inline>
              <b-form-input
                id="input-1"
                type="text"
                v-model="newBudgetCategory"
                placeholder="Enter new category"
                required
              ></b-form-input>
              <b-button @click="addBudgetCategory">Add</b-button>
            </b-form>
          </b-list-group-item>
        </b-list-group>
      </b-col>
    </div>
  </div>
</template>

<script>
import Vue from 'vue'

export default Vue.extend({
  mounted() {
    this.getBudgetCategories()
    this.getBudgetEntries()
  },
  methods: {
    async addBudgetCategory() {
      const cat = {
        name: this.newBudgetCategory,
        type: this.selected_importance
      }
      await this.$axios.post('/budget/category', cat)
      this.getBudgetCategories()
    },

    async getBudgetCategories() {
      const categories = await this.$axios.$get('/budget/category')

      let new_categories = []
      categories.budget_categories.forEach((cat) => {
        new_categories.push({ text: cat.name, value: cat.id })
      })
      this.budget_categories = new_categories
      this.form.category_id = new_categories[0].value
    },
    async addBudgetEntry() {
      const entry = {
        name: this.form.name,
        amount: this.form.amount,
        category_id: this.form.category_id,
        importance: this.form.importance
      }
      await this.$axios.post('/budget', entry)
      this.getBudgetEntries()
    },

    async getBudgetEntries() {
      const entries = await this.$axios.$get('/budget')
      this.budget_entries = entries.budget
    }
  },
  data() {
    return {
      form: {
        name: '',
        amount: null,
        category_id: 0,
        importance: 'essential'
      },
      importance: ['essential', 'discretionary', 'excess'],
      budget_categories: [],
      fields: ['name', 'category', 'budget_amount', 'importance'],
      budget_entries: []
    }
  }
})
</script>
