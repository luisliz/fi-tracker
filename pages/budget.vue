<template>
  <div>
    <div class="row">
      <div>
        <b-form-datepicker id="example-datepicker" v-model="value" class="mb-2"></b-form-datepicker>
      </div>
      <div>
        <b-form-input placeholder="Name"></b-form-input>
      </div>
      <div>
        <b-form-select v-model="selectedtype" :options="types"></b-form-select>
      </div>
      <div>
        <b-form-select v-model="selectedimportance" :options="importance"></b-form-select>
      </div>
      <div>
        <b-form-input placeholder="Amount"></b-form-input>
      </div>
      <div>
        <b-button variant="primary">Add</b-button>
      </div>
    </div>
    <b-table hover :items="items" :fields="fields" striped responsive="sm"></b-table>


  </div>
</template>

<script>
export default {
  data() {
    return {
      selectedtype: 'Savings',
      selectedimportance: 'Essential',
      types: [
        'Savings',
        'Services',
        'Transportation'
      ],
      importance: [
        'Essential',
        'Discretionary',
        'Excess',
      ],
      fields: ['name', 'type', 'budget', 'importance'],
      items: [
        {importance: 'Essential', type: 'Savings', name: 'Savings', budget: '$40.00'},
        {importance: 'Essential', type: 'Services', name: 'Internet', budget: '$89.99'},
        {importance: 'Excess', type: 'Transportation', name: 'Car', budget: '$399.40'},
        {importance: 'Discretionary', type: 'Services', name: 'Utilities', budget: '$10.40'},
        {importance: '', type: 'Wellness', name: 'Haircut', budget: '$10.40'},
        {importance: '', type: 'Shelter', name: 'Apartment', budget: '$3100.0'}
      ],
    }
  }
}
</script>
