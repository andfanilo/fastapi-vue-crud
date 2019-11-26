import { shallowMount } from "@vue/test-utils";
import BooksTable from "../../src/components/BooksTable";

describe("BooksTable.vue", () => {
  it("renders props.heading when passed", () => {
    const heading = "new message";
    const wrapper = shallowMount(BooksTable, {
      propsData: { heading }
    });
    expect(wrapper.text()).toMatch(heading);
  });
});
