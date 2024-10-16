import module_a, module_base, module_b

def main():
    base_object = module_base.Base("name")

    base_object_with_a = module_a.add_a(base_object)
    base_object_with_a.a.fooa()

    base_object_with_a_and_b = module_b.add_b(base_object_with_a)
    base_object_with_a_and_b.b.foob()


    
if __name__ == "__main__":
    main()