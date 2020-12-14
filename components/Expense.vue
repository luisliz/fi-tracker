<template>
  <div>
    <h4>Expense</h4>
    <div class="row">
      <div>
        <b-form-datepicker id="example-datepicker" v-model="value" class="mb-2"></b-form-datepicker>
      </div>
      <div>
        <b-form-input placeholder="Amount"></b-form-input>
      </div>
      <div>
        <b-form-input placeholder="Amount"></b-form-input>
      </div>
      <div>
        <b-button variant="primary">Add</b-button>
      </div>

    </div>
  </div>
</template>

<style>
.NuxtLogo {
  animation: 1s appear;
  margin: auto;
}

@keyframes appear {
  0% {
    opacity: 0;
  }
}
</style>
