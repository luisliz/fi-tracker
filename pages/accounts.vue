<template>
  <div class="container">
    <div>
      <div class="row">
        <h4>Assets</h4>
        <b-button variant="primary">Add</b-button>
      </div>
      <div class="row">
        <Account accName="BPPR" accType="Credit Card" amount="3448"/>
        <Account accName="BPPR" accType="Credit Card" amount="3448"/>
        <Account accName="BPPR" accType="Credit Card" amount="3448"/>
        <Account accName="BPPR" accType="Credit Card" amount="3448"/>
      </div>
      <div class="row">
        <h4>Liabilities</h4>
        <b-button variant="primary">Add</b-button>
      </div>
      <div class="row">
        <Account accName="BPPR" accType="Credit Card" amount="3895" accIsLiability/>
        <Account accName="BPPR" accType="Credit Card" amount="3895" accIsLiability/>
        <Account accName="BPPR" accType="Credit Card" amount="3895" accIsLiability/>
        <Account accName="BPPR" accType="Credit Card" amount="3895" accIsLiability/>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import Vue from 'vue'

export default Vue.extend({})
</script>

<style>
.container {
  /*margin: 0 auto;*/
  /*min-height: 100vh;*/
  /*display: flex;*/
  /*justify-content: center;*/
  /*align-items: center;*/
  /*text-align: center;*/
}
</style>
