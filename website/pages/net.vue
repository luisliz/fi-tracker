<template>
  <div>
    <div class="row">
      <div>
        <b-form-datepicker id="example-datepicker" v-model="value" class="mb-2"></b-form-datepicker>
      </div>
      <div>
        <b-form-select v-model="selectedexpense" :options="expenses"></b-form-select>
      </div>
      <div>
        <b-form-select v-model="selectedaccount" :options="accounts"></b-form-select>
      </div>
      <div>
        <b-form-input placeholder="Store"></b-form-input>
      </div>
      <div>
        <b-form-input placeholder="Amount"></b-form-input>
      </div>
      <div>
        <b-button variant="primary">Add</b-button>
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
import DoughnutChart from '~/components/DoughnutChart'
import StackedLineChart from '~/components/StackedLineChart'
export default {
  components: { StackedLineChart, DoughnutChart },
  data() {
    return {
      selectedexpense: 'apartment',
      expenses: [
        'haircut',
        'apartment',
        'car',
        'pets'
      ],
      selectedaccount: 'BPPR',
      accounts: [
        'BPPR',
        'Chase',
        'Discover'
      ],
      fields: ['type', 'account', 'amount', 'date', 'store', 'show_details'],
      items: [
        {
          isActive: false,
          _showDetails: false,
          type: 'Apartment',
          account: 'BPPR',
          store: 'Apartments.com',
          amount: '$5802',
          date: '05/05/2020',
          budget: '$50159',
          year_average: '$4504',
          annual: '5905',
          savings: '0'
        },
        {
          isActive: false,
          _showDetails: false,
          type: 'Car',
          account: 'Discover',
          store: 'CarDealersPR',
          amount: '$5802',
          date: '05/05/2020'
        },
        {
          isActive: false,
          _showDetails: false,
          type: 'Internet',
          account: 'Chase',
          store: 'Liberty',
          amount: '$5802',
          date: '05/05/2020'
        }
      ]
    }
  }
}
</script>
