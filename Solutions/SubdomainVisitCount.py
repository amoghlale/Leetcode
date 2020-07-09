class Solution:
    def create_output_dict(self, field, count, output_dict):
        if field in output_dict:
            output_dict[field] += int(count)
        else:
            output_dict[field] = int(count)
        return output_dict

    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        output_dict = {}
        for i in cpdomains:
            count, domain = i.split()
            subdomain_list = domain.split(".")
            output_dict = self.create_output_dict('.'.join(subdomain_list), count, self.create_output_dict(subdomain_list[-1], count, output_dict))
            if len(subdomain_list) == 3:
                output_dict = self.create_output_dict('.'.join(subdomain_list[1:]), count, output_dict)

        return ["{} {}".format(str(value), key) for key, value in output_dict.items()]
