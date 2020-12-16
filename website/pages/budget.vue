<template>
  <div class="m-3 row">

    <div class="col-9">
      <div class="row">
        <div>
          <b-form-input v-model="form.name" placeholder="Name"></b-form-input>
        </div>
        <div>
          <b-form-select v-model="form.category_id" :options="budget_categories"></b-form-select>
        </div>
        <div>
          <b-form-select v-model="form.importance" :options="importance"></b-form-select>
        </div>
        <div>
          <b-form-input v-model="form.amount" placeholder="Amount"></b-form-input>
        </div>
        <div>
          <b-button variant="primary" @click="addBudgetEntry">Add</b-button>
        </div>
      </div>
      <b-table hover :items="budget_entries" :fields="fields" striped responsive="sm"></b-table>
    </div>
    <div class="col-3">
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
              v-model="newBudgetCategory" addBudgetCategory
              placeholder="Enter new category"
              required
            ></b-form-input>
            <b-button @click="addBudgetCategory">Add</b-button>
          </b-form>
        </b-list-group-item>
      </b-list-group>
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
